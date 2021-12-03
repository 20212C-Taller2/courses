from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import BaseModelDb


class Exam(BaseModelDb):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    questions = relationship("Question", backref="exam", lazy="joined")


class Question(BaseModelDb):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, nullable=False)
    exam_id = Column(Integer, ForeignKey('exams.id'))
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
