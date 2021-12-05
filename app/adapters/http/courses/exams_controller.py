from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.adapters.database.courses import sql_course_repository, sql_exam_repository
from app.dependencies import get_db
from app.domain.courses.model import exams

router = APIRouter(
    prefix='/courses/{course_id}/exams',
    tags=["Exams"],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)


@router.post("", response_model=exams.Exam, status_code=status.HTTP_201_CREATED)
def create_exam(course_id: int, exam: exams.Exam,
                db: Session = Depends(get_db)):
    course = sql_course_repository.get_course(db=db, course_id=course_id)

    return sql_exam_repository.create_exam(db=db, course_id=course.id, exam_model=exam)


@router.get("", response_model=List[exams.Exam], status_code=status.HTTP_200_OK)
def get_course_exams(course_id: int, db: Session = Depends(get_db)) -> List[exams.Exam]:
    return sql_exam_repository.get_course_exams(db=db, course_id=course_id)
