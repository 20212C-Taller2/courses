from itertools import zip_longest
from typing import List

from sqlalchemy.orm import Session

from app.adapters.database.courses import model
from app.domain.exams.exam_exceptions import ExamsNotFoundError, SubmittedExamsNotFoundError
from app.domain.exams.exams import ExamCreate as ExamModel, Exam
from app.domain.exams.submitted_exam import SubmittedExam, RevisedExam


def create_exam(db: Session, course_id: int, exam_model: ExamModel):
    db_course = db.query(model.Course).get(course_id)

    db_exam = model.Exam(course_id=course_id, title=exam_model.title, published=exam_model.published)
    db_course.exams.append(db_exam)

    questions = [model.Question(number=question.number,
                                text=question.text)
                 for question in exam_model.questions]

    for question in questions:
        db_exam.questions.append(question)

    db.commit()
    db.refresh(db_exam)

    return db_exam.to_entity()


def get_course_exams(db: Session, course_id: int, published: bool) -> List[ExamModel]:
    exams_query = db.query(model.Exam) \
        .filter(model.Exam.course_id == course_id)

    if published is not None:
        exams_query = exams_query.filter(model.Exam.published == published)

    db_course_exams = exams_query \
        .order_by(model.Exam.id) \
        .all()

    if len(db_course_exams) == 0:
        raise ExamsNotFoundError(course_id)

    return [db_course_exam.to_entity() for db_course_exam in db_course_exams]


def submit_exam(db: Session, course_id: int, exam_id: int, submitted_exam: SubmittedExam):
    # db_exam = db.query(model.Exam).get(exam_id)

    db_submitted_exam = model.SubmittedExam(student_id=submitted_exam.student,
                                            course_id=course_id,
                                            exam_id=exam_id)

    db.add(db_submitted_exam)

    for answer in submitted_exam.answers:
        db_answer = model.Answer(question_id=answer.question_id,
                                 text=answer.text)
        db_submitted_exam.answers.append(db_answer)

    db.commit()
    db.refresh(db_submitted_exam)

    return db_submitted_exam.to_entity()


def save_review_exam(db: Session, submitted_exam_id: int, revised_exam: RevisedExam):
    db_reviewed_exam = model.RevisedExam(submitted_exam_id=submitted_exam_id,
                                         reviewer_id=revised_exam.review.user,
                                         feedback=revised_exam.review.feedback,
                                         grade=revised_exam.review.grade)

    db.add(db_reviewed_exam)
    db.commit()
    db.refresh(db_reviewed_exam)

    return db_reviewed_exam


def get_submmited_exam(db: Session, submitted_exam_id) -> RevisedExam:
    db_submitted_exam = db.query(model.SubmittedExam).get(submitted_exam_id)

    return db_submitted_exam.to_entity()


def get_submmited_exams(db: Session, course_id: int, student_id: str, exam_id: int,
                        skip: int = 0, limit: int = 100) -> List[RevisedExam]:
    db_submitted_exams_query = db.query(model.SubmittedExam) \
        .filter(model.SubmittedExam.course_id == course_id)

    if student_id:
        db_submitted_exams_query = db_submitted_exams_query.filter(model.SubmittedExam.student_id == student_id)

    if exam_id:
        db_submitted_exams_query = db_submitted_exams_query.filter(model.SubmittedExam.exam_id == exam_id)

    db_submitted_exams = db_submitted_exams_query \
        .order_by(model.SubmittedExam.id) \
        .offset(skip) \
        .limit(limit) \
        .all()

    if len(db_submitted_exams) == 0:
        raise SubmittedExamsNotFoundError()

    return [db_submitted_exam.to_entity() for db_submitted_exam in db_submitted_exams]


def update_exam(db: Session, exam_id: int, edited_exam: Exam):
    db_exam = db.query(model.Exam).get(exam_id)

    for var, value in vars(edited_exam).items():
        setattr(db_exam, var, value) if (value and not isinstance(value, list)) else None

    for db_question, edited_question in zip_longest(db_exam.questions, edited_exam.questions):
        if db_question is not None and edited_question is not None:
            for var, value in vars(edited_question).items():
                setattr(db_question, var, value) if value else None
        elif db_question is not None and edited_question is None:
            db_exam.questions.remove(db_question)
        elif db_question is None and edited_question is not None:
            db_exam.questions.append(model.Question(number=edited_question.number,
                                                    text=edited_question.text))

    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)

    return db_exam.to_entity()
