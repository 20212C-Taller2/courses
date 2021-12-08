from pydantic import BaseModel, constr

from app.domain.exams.questions import QuestionCreate

class AnswerCreate(BaseModel):
    question_id: int
    text: constr(min_length=1)

class Answer(BaseModel):
    question: QuestionCreate
    text: constr(min_length=1)

    class Config:
        orm_mode = True
