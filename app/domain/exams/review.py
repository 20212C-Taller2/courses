from pydantic import BaseModel, conint


class Review(BaseModel):
    user: str
    role: str
    grade: conint(gt=0, le=10)

    class Config:
        orm_mode = True
