"""
Estos son los "modelos" de pydantic que son usados por la api para validar
campos
"""
from typing import Optional, Set

from pydantic import BaseModel, constr
from pydantic.class_validators import List

from app.domain.courses.model.course_type import CourseType


class CourseBase(BaseModel):
    title: constr(min_length=1)
    description: Optional[str] = None
    subscription: str
    type: CourseType
    creator: constr(min_length=1)
    location: Optional[str]
    tags: Set[str] = set()
    media: Set[str] = set()

    class Config:
        orm_mode = True


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    students: Set[str] = set()
    collaborators: Set[str] = set()
    exams: List = []

    class Config:
        orm_mode = True

    def enroll_student(self, student):
        self.students.add(student)

    def register_collaborator(self, collaborator):
        self.collaborators.add(collaborator)
