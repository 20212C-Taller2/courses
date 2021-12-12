from typing import Optional

from pydantic import BaseModel, conint


class Review(BaseModel):
    user: str
    feedback: Optional[str] = None
    grade: conint(gt=0, le=10)

    class Config:
        orm_mode = True
