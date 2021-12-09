from pydantic import BaseModel, constr

from app.domain.exams.questions import Question


class AnswerCreate(BaseModel):
    question_id: int
    text: constr(min_length=1)


class Answer(BaseModel):
    question: Question
    text: constr(min_length=1)

    class Config:
        orm_mode = True
