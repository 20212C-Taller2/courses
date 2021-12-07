from pydantic import BaseModel, PositiveInt, constr


class Question(BaseModel):
    number: PositiveInt
    text: constr(min_length=1)

    class Config:
        orm_mode = True
