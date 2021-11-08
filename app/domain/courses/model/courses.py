"""
Estos son los "modelos" de pydantic que son usados por la api para validar
campos
"""
from typing import Optional, Set

from pydantic import BaseModel, PositiveInt, constr

from app.domain.courses.model.course_type import CourseType
from app.domain.courses.model.subscription import Subscription


class CourseBase(BaseModel):
    title: constr(min_length=1)
    description: Optional[str] = None
    exams: PositiveInt
    subscription: Subscription
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

    class Config:
        orm_mode = True
