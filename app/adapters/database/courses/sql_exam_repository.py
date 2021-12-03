from sqlalchemy.orm import Session

from app.adapters.database.courses import model, exam
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
