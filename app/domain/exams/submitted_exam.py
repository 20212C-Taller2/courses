from pydantic import BaseModel, conlist, constr

from app.domain.exams.answer import Answer


class SubmittedExam(BaseModel):
    student: constr(min_length=1)
    answers: conlist(Answer, min_items=1)

    class Config:
        orm_mode = True
