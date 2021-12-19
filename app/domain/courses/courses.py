"""
Estos son los "modelos" de pydantic que son usados por la api para validar
campos
"""
from typing import Optional, Set

from pydantic import BaseModel, constr
from pydantic.class_validators import List

from app.domain.courses.course_type import CourseType
from app.domain.courses.enrollment import Enrollment
from app.domain.courses.enrollment_exceptions import CreatorEnrollmentError, CollaboratorEnrollmentError, \
    CreatorRegisterError, StudentRegisterError, StudentAlreadyEnrolledError, CollaboratorAlreadyRegisteredError


class CourseBase(BaseModel):
    title: constr(min_length=1)
    description: Optional[str] = None
    type: CourseType
    creator: constr(min_length=1)
    location: Optional[str]
    tags: Set[str] = set()
    media: Set[str] = set()

    class Config:
        orm_mode = True


class CourseCreate(CourseBase):
    subscription: str


class Course(CourseCreate):
    id: int
    students: Set[str] = set()
    collaborators: Set[str] = set()
    exams: List = []

    class Config:
        orm_mode = True

    def enroll_student(self, new_student) -> Enrollment:
        if self.creator == new_student:
            raise CreatorEnrollmentError(new_student)
        elif new_student in self.collaborators:
            raise CollaboratorEnrollmentError(new_student)
        elif new_student in self.students:
            raise StudentAlreadyEnrolledError(new_student)

        self.students.add(new_student)

        return Enrollment(student_id=new_student, course_id=self.id)

    def register_collaborator(self, new_collaborator):
        if new_collaborator == self.creator:
            raise CreatorRegisterError(new_collaborator)
        elif new_collaborator in self.students:
            raise StudentRegisterError(new_collaborator)
        elif new_collaborator in self.collaborators:
            raise CollaboratorAlreadyRegisteredError(new_collaborator)

        self.collaborators.add(new_collaborator)
