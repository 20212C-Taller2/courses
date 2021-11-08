"""
Modelos para el ORM de la base de datos
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY
from app.db.database import BaseModelDb


class Course(BaseModelDb):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    exams = Column(Integer, nullable=False)
    subscription = Column(String, nullable=False)
    type = Column(String, nullable=False)
    creator = Column(String, nullable=False)
    location = Column(String, nullable=True)
    tags = Column(ARRAY(String), nullable=False)
    media = Column(ARRAY(String), nullable=False)


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
