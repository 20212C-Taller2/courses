from typing import List, Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.adapters.database.courses import sql_course_repository, sql_exam_repository
from app.dependencies import get_session
from app.domain.exams import exams
from app.domain.exams.review import Review
from app.domain.exams.submitted_exam import RevisedExam, SubmittedExamCreate
from app.ports.logger import logger

router = APIRouter(
    prefix='/courses/{course_id}/exams',
    tags=["Exams"],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)


@router.post("", response_model=exams.Exam, status_code=status.HTTP_201_CREATED)
def create_exam(course_id: int, exam: exams.ExamCreate,
                db: Session = Depends(get_session)):
    logger.info(f'Nuevo examen en curso {course_id}')
    course = sql_course_repository.get_course(db=db, course_id=course_id)

    return sql_exam_repository.create_exam(db=db, course_id=course.id, exam_model=exam)


@router.get("", response_model=List[exams.Exam], status_code=status.HTTP_200_OK)
def get_course_exams(course_id: int, published: Optional[bool] = None,
                     db: Session = Depends(get_session)) -> List[exams.ExamCreate]:
    return sql_exam_repository.get_course_exams(db=db, course_id=course_id, published=published)


@router.put("/{exam_id}", response_model=exams.Exam, status_code=status.HTTP_200_OK)
def edit_exam(exam_id: int, exam: exams.ExamCreate,
              db: Session = Depends(get_session)):
    return sql_exam_repository.update_exam(db, exam_id, exam)


@router.post("/{exam_id}", status_code=status.HTTP_201_CREATED)
def submit_exam(course_id: int, exam_id: int, submitted_exam: SubmittedExamCreate,
                db: Session = Depends(get_session)):
    # TODO: Validaciones
    #   - Obtener el curso
    #   - Que el examen pertenezca al curso
    #   - Que el estudiante se encuentre inscripto al curso y no haya enviado una respuesta al examen previamente
    #   - Que conteste todas las preguntas del examen
    #   - Mejorar response_model

    return sql_exam_repository.submit_exam(db, course_id, exam_id, submitted_exam)


@router.patch("/{submitted_exam_id}", response_model=RevisedExam, status_code=status.HTTP_200_OK)
def review_exam(course_id: int, submitted_exam_id: int, review: Review,
                db: Session = Depends(get_session)):
    submitted_exam = sql_exam_repository.get_submmited_exam(db, submitted_exam_id)

    revised_exam = submitted_exam.correct(review)

    sql_exam_repository.save_review_exam(db, submitted_exam_id, revised_exam)

    return revised_exam


@router.get("/submissions", response_model=List[RevisedExam], status_code=status.HTTP_200_OK)
def get_submitted_exams(course_id: int, student_id: Optional[str] = None, exam_id: Optional[int] = None,
                        skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return sql_exam_repository.get_submmited_exams(db, course_id, student_id, exam_id, skip, limit)
