from typing import List

from sqlalchemy.orm import Session

from app.adapters.database.courses import model
from app.domain.exams.exam_exceptions import ExamsNotFoundError
from app.domain.exams.exams import ExamCreate as ExamModel
from app.domain.exams.submitted_exam import SubmittedExam, RevisedExam


def create_exam(db: Session, course_id: int, exam_model: ExamModel):
    db_course = db.query(model.Course).get(course_id)

    db_exam = model.Exam(course_id=course_id, title=exam_model.title)
    db_course.exams.append(db_exam)

    questions = [model.Question(number=question.number,
                                text=question.text)
                 for question in exam_model.questions]

    for question in questions:
        db_exam.questions.append(question)

    db.commit()
    db.refresh(db_exam)

    return db_exam.to_entity()


def get_course_exams(db: Session, course_id: int) -> List[ExamModel]:
    db_course_exams = db.query(model.Exam) \
        .filter(model.Exam.course_id == course_id) \
        .order_by(model.Exam.id) \
        .all()

    if len(db_course_exams) == 0:
        raise ExamsNotFoundError(course_id)

    return [db_course_exam.to_entity() for db_course_exam in db_course_exams]


def submit_exam(db: Session, course_id: int, exam_id: int, submitted_exam: SubmittedExam):
    db_exam = db.query(model.Exam).get(exam_id)

    db_submitted_exam = model.SubmittedExam(student_id=submitted_exam.student,
                                            course_id=course_id,
                                            exam_id=exam_id)

    db.add(db_submitted_exam)

    for answer in submitted_exam.answers:
        question = filter(lambda q: answer.question.text == q.text, db_exam.questions)
        db_answer = model.Answer(question_id=list(question)[0].id,
                                 text=answer.text)
        db_submitted_exam.answers.append(db_answer)

    db.commit()
    db.refresh(db_submitted_exam)

    return db_submitted_exam


def save_review_exam(db: Session, submitted_exam_id: int, revised_exam: RevisedExam):
    db_reviewed_exam = model.RevisedExam(submitted_exam_id=submitted_exam_id,
                                         reviewer_id=revised_exam.review.user,
                                         reviewer_role=revised_exam.review.role,
                                         grade=revised_exam.review.grade)

    db.add(db_reviewed_exam)
    db.commit()
    db.refresh(db_reviewed_exam)

    return db_reviewed_exam


def get_submmited_exam(db: Session, submitted_exam_id) -> SubmittedExam:
    db_submitted_exam = db.query(model.SubmittedExam).get(submitted_exam_id)

    return db_submitted_exam.to_entity()
