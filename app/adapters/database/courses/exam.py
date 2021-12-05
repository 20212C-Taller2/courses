from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import BaseModelDb
from app.domain.courses.model.exams import Exam as ExamModel
from app.domain.courses.model.questions import Question as QuestionModel


class Exam(BaseModelDb):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    questions = relationship("Question", backref="exam", lazy="joined")

    def to_entity(self) -> ExamModel:
        return ExamModel(
            title=self.title,
            questions=[question.to_entity() for question in self.questions]
        )


class Question(BaseModelDb):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, nullable=False)
    exam_id = Column(Integer, ForeignKey('exams.id'))
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def to_entity(self) -> QuestionModel:
        return QuestionModel(
            number=self.number,
            text=self.text
        )
