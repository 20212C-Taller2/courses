from typing import Optional

from pydantic import BaseModel, conlist, constr

from app.domain.exams.answer import AnswerCreate, Answer
from app.domain.exams.review import Review


class SubmittedExamCreate(BaseModel):
    student: constr(min_length=1)
    answers: conlist(AnswerCreate, min_items=1)

    class Config:
        orm_mode = True


class SubmittedExam(BaseModel):
    id: int
    exam_id: int
    student: constr(min_length=1)
    answers: conlist(Answer, min_items=1)

    class Config:
        orm_mode = True

    def correct(self, review: Review):
        return RevisedExam(id=self.id,
                           exam_id=self.exam_id,
                           student=self.student,
                           answers=self.answers,
                           review=review)


class RevisedExam(SubmittedExam):
    review: Optional[Review] = None
