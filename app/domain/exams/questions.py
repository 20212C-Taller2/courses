from pydantic import BaseModel, PositiveInt, constr


class QuestionCreate(BaseModel):
    number: PositiveInt
    text: constr(min_length=1)

    class Config:
        orm_mode = True


class Question(QuestionCreate):
    id: int

    class Config:
        orm_mode = True
