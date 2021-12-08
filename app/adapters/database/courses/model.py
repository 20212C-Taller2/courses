"""
Modelos para el ORM de la base de datos
"""

from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY

from app.db.database import BaseModelDb
from app.domain.courses.courses import Course as ModelCourse
from app.domain.exams.answer import Answer as AnswerModel
from app.domain.exams.exams import Exam as ExamModel
from app.domain.exams.questions import Question as QuestionModel
from app.domain.exams.submitted_exam import SubmittedExam as SubmittedExamModel


class Course(BaseModelDb):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    subscription = Column(String, nullable=False)
    type = Column(String, nullable=False)
    creator = Column(String, nullable=False)
    location = Column(String, nullable=True)
    tags = Column(ARRAY(String), nullable=False)
    media = Column(ARRAY(String), nullable=False)
    students = relationship("Student", backref="course")
    collaborators = relationship("Collaborator", cascade="all,delete", backref="course")
    exams = relationship("Exam", backref="course", lazy="joined")

    def to_entity(self) -> ModelCourse:
        return ModelCourse(
            id=self.id,
            title=self.title,
            description=self.description,
            subscription=self.subscription,
            type=self.type,
            creator=self.creator,
            location=self.location,
            tags=self.tags,
            media=self.media,
            students={student.id for student in self.students},
            collaborators={student.id for student in self.collaborators},
            exams=[exam.to_entity() for exam in self.exams]
        )


class Student(BaseModelDb):
    __tablename__ = "students"

    id = Column(String, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)


class Collaborator(BaseModelDb):
    __tablename__ = "collaborators"

    id = Column(String, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)


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
            id=self.id,
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

    def to_entity(self) -> SubmittedExamModel:
        return SubmittedExamModel(student=self.student_id,
                                  answers=[answer.to_entity() for answer in self.answers])


class RevisedExam(BaseModelDb):
    __tablename__ = "revised_exams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    submitted_exam_id = Column(Integer, ForeignKey('submitted_exams.id'))
    reviewer_id = Column(String, nullable=False)
    reviewer_role = Column(String, nullable=False)
    grade = Column(Integer, nullable=False)


class Answer(BaseModelDb):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    submitted_exam_id = Column(Integer, ForeignKey('submitted_exams.id'))
    text = Column(String, nullable=False)
    question = relationship("Question", backref="answer")

    def to_entity(self):
        return AnswerModel(question=self.question.to_entity(),
                           text=self.text)

# class Tag(BaseModelDb):
#     __tablename__ = "tags"
#
#     name = Column(String, primary_key=True, index=True)
#     course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True, nullable=False)
#
#     course = relationship("Course", uselist=True, back_populates="tags")
#
#
# class Media(BaseModelDb):
#     __tablename__ = "media"
#
#     url = Column(String, primary_key=True, index=True)
#     course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True, nullable=False)
#
#     course = relationship("Course", back_populates="media")
