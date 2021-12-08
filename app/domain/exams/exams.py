from pydantic import BaseModel, constr, conlist

from app.domain.exams.questions import QuestionCreate, Question


class ExamCreate(BaseModel):
    title: constr(min_length=1)
    questions: conlist(QuestionCreate, min_items=1)

    class Config:
        orm_mode = True


class Exam(ExamCreate):
    id: int
    questions: conlist(Question, min_items=1)

    class Config:
        orm_mode = True
