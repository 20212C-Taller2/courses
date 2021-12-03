from pydantic import BaseModel, constr, conlist

from app.domain.courses.model.questions import Question


class Exam(BaseModel):
    title: constr(min_length=1)
    questions: conlist(Question, min_items=1)

    class Config:
        orm_mode = True
