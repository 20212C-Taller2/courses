from datetime import datetime

from pydantic import BaseModel, constr


class Enrollment(BaseModel):
    student_id: constr(min_length=1)
    course_id: int
    date_time: datetime = datetime.now()

    class Config:
        orm_mode = True
