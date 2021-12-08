from app.domain.exams.submitted_exam import SubmittedExam
from tests.examples.answer_example import AnswerExample


class SubmittedExamExample:
    def __init__(self):
        self.student = 'student@example.com'
        self.answers = [AnswerExample().build()]

    def build(self):
        return SubmittedExam(student=self.student,
                             answers=self.answers)

    def with_student(self, student):
        self.student = student
        return self

    def with_answers(self, answers):
        self.answers = answers
        return self
