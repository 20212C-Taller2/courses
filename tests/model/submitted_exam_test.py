import unittest

from pydantic import ValidationError

from app.domain.exams.submitted_exam import SubmittedExam
from tests.examples.answer_example import AnswerExample


class TestSubmittedExamUseCase(unittest.TestCase):
    def test_submitted_exam_attributes(self):
        submitted_exam = SubmittedExam(student='student@example.com',
                                       answers=[AnswerExample().build()])

        self.assertIsInstance(submitted_exam.student, str)
        self.assertIsInstance(submitted_exam.answers, list)

    def test_submitted_exam_student_should_not_be_empty(self):
        def submitted_exam_without_student():
            return SubmittedExam(student='',
                                 answers=[AnswerExample().build()])

        self.assertRaises(ValidationError, submitted_exam_without_student)

    def test_submitted_exam_answers_should_not_be_empty(self):
        def submitted_exam_without_answers():
            return SubmittedExam(student='student@example.com',
                                 answers=[])

        self.assertRaises(ValidationError, submitted_exam_without_answers)


if __name__ == '__main__':
    unittest.main()
