from typing import List

from sqlalchemy.orm import Session

from app.adapters.database.courses import model, exam
from app.domain.exams.exam_exceptions import ExamsNotFoundError
from app.domain.exams.exams import ExamCreate as ExamModel
from app.domain.exams.submitted_exam import SubmittedExam


def create_exam(db: Session, course_id: int, exam_model: ExamModel):
    db_course = db.query(model.Course).get(course_id)

    db_exam = exam.Exam(course_id=course_id, title=exam_model.title)
    db_course.exams.append(db_exam)

    questions = [exam.Question(number=question.number,
                               text=question.text)
                 for question in exam_model.questions]

    for question in questions:
        db_exam.questions.append(question)

    db.commit()
    db.refresh(db_exam)

    return db_exam.to_entity()


def get_course_exams(db: Session, course_id: int) -> List[ExamModel]:
    db_course_exams = db.query(exam.Exam) \
        .filter(exam.Exam.course_id == course_id) \
        .order_by(exam.Exam.id) \
        .all()

    if len(db_course_exams) == 0:
        raise ExamsNotFoundError(course_id)

    return [db_course_exam.to_entity() for db_course_exam in db_course_exams]


def submit_exam(db: Session, course_id: int, exam_id: int, submitted_exam: SubmittedExam):
    db_exam = db.query(exam.Exam).get(exam_id)

    db_submitted_exam = exam.SubmittedExam(student_id=submitted_exam.student,
                                           course_id=course_id,
                                           exam_id=exam_id)

    db.add(db_submitted_exam)

    for answer in submitted_exam.answers:
        question = filter(lambda q: answer.question.text == q.text, db_exam.questions)
        db_answer = exam.Answer(question_id=list(question)[0].id,
                                text=answer.text)
        db_submitted_exam.answers.append(db_answer)

    db.commit()
    db.refresh(db_submitted_exam)

    return db_submitted_exam
