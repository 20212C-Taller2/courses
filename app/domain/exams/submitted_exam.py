from pydantic import BaseModel, conlist, constr
from pydantic.dataclasses import dataclass

from app.domain.exams.answer import AnswerCreate, Answer
from app.domain.exams.review import Review


class SubmittedExamCreate(BaseModel):
    student: constr(min_length=1)
    answers: conlist(AnswerCreate, min_items=1)

    class Config:
        orm_mode = True


class SubmittedExam(BaseModel):
    student: constr(min_length=1)
    answers: conlist(Answer, min_items=1)

    class Config:
        orm_mode = True

    def correct(self, review: Review):
        return RevisedExam(self, review)


@dataclass
class RevisedExam:
    submitted_exam: SubmittedExam
    review: Review

    def __init__(self, submitted_exam: SubmittedExam, review: Review):
        self.submitted_exam = submitted_exam
        self.review = review
