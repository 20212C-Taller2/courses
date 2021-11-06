"""
Estos son los "modelos" de pydantic que son usados por la api para validar
campos
"""
from typing import Optional

from app.domain.courses.model.subscription import Subscription
from app.domain.courses.model.course_type import CourseType
from pydantic import BaseModel, PositiveInt, constr


class CourseBase(BaseModel):
    title: constr(min_length=1)
    description: Optional[str] = None
    exams: PositiveInt
    subscription: Subscription
    type: CourseType


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True
