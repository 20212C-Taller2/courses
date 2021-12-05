from typing import List

from sqlalchemy.orm import Session

from app.adapters.database.courses import model, exam
from app.domain.courses.model.exam_exceptions import ExamsNotFoundError
from app.domain.courses.model.exams import Exam as ExamModel


def create_exam(db: Session, course_id: int, exam_model: ExamModel):
    db_course = db.query(model.Course).get(course_id)

    db_exam = exam.Exam(id=len(db_course.exams) + 1, title=exam_model.title)
    db_course.exams.append(db_exam)

    questions = [exam.Question(course_id=course_id,
                               number=question.number,
                               text=question.text) for question in exam_model.questions]

    for question in questions:
        db_exam.questions.append(question)

    db.commit()
    db.refresh(db_exam)

    return db_exam


def get_course_exams(db: Session, course_id: int) -> List[ExamModel]:
    db_course_exams = db.query(exam.Exam) \
        .filter(exam.Exam.course_id == course_id) \
        .order_by(exam.Exam.id) \
        .all()

    if len(db_course_exams) == 0:
        raise ExamsNotFoundError(course_id)

    return [db_course_exam.to_entity() for db_course_exam in db_course_exams]
