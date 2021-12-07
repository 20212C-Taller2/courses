from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from app.adapters.database.courses.model import Student
from app.db.database import BaseModelDb
from app.domain.exams.exams import Exam as ExamModel
from app.domain.exams.questions import Question as QuestionModel


class Exam(BaseModelDb):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    questions = relationship("Question", backref="exam", lazy="joined")

    def to_entity(self) -> ExamModel:
        return ExamModel(
            id=self.id,
            title=self.title,
            questions=[question.to_entity() for question in self.questions]
        )


class Question(BaseModelDb):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    exam_id = Column(Integer, ForeignKey('exams.id'))
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def to_entity(self) -> QuestionModel:
        return QuestionModel(
            number=self.number,
            text=self.text
        )


class SubmittedExam(BaseModelDb):
    __tablename__ = "submitted_exams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String)
    course_id = Column(Integer)
    exam_id = Column(Integer, ForeignKey('exams.id'))
    answers = relationship("Answer", backref="submitted_exam", lazy="joined")

    __table_args__ = (ForeignKeyConstraint([student_id, course_id],
                                           [Student.id, Student.course_id]),
                      {})


class Answer(BaseModelDb):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    submitted_exam_id = Column(Integer, ForeignKey('submitted_exams.id'))
    text = Column(String, nullable=False)
