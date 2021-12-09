from app.domain.exams.submitted_exam import SubmittedExam
from tests.examples.answer_example import AnswerExample


class SubmittedExamExample:
    def __init__(self):
        self.id = 1
        self.exam_id = 1
        self.student = 'student@example.com'
        self.answers = [AnswerExample().build()]

    def build(self):
        return SubmittedExam(id=self.id,
                             exam_id=self.exam_id,
                             student=self.student,
                             answers=self.answers)

    def with_id(self, new_id: int):
        self.id = new_id
        return self

    def with_exam_id(self, exam_id: int):
        self.exam_id = exam_id
        return self

    def with_student(self, student):
        self.student = student
        return self

    def with_answers(self, answers):
        self.answers = answers
        return self
