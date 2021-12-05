"""
Modelos para el ORM de la base de datos
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY

from app.db.database import BaseModelDb
from app.domain.courses.model.courses import Course as ModelCourse


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
