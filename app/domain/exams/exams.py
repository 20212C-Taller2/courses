from pydantic import BaseModel, constr, conlist

from app.domain.exams.questions import Question


class ExamCreate(BaseModel):
    title: constr(min_length=1)
    questions: conlist(Question, min_items=1)

    class Config:
        orm_mode = True


class Exam(ExamCreate):
    id: int

    class Config:
        orm_mode = True
