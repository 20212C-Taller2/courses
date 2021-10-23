"""
Estos son los "modelos" de pydantic que son usados por la api para validar
campos
"""
from typing import Optional

from pydantic import BaseModel, PositiveInt


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    exams: PositiveInt


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True
