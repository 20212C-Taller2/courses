import unittest

from pydantic import ValidationError

from app.domain.exams.exams import ExamCreate
from tests.examples.question_example import QuestionExample


class TestExamUseCase(unittest.TestCase):
    def test_exam_attributes(self):
        exam = ExamCreate(title='title', questions=[QuestionExample().build()])

        self.assertIsInstance(exam.title, str)
        self.assertIsInstance(exam.questions, list)

    def test_exam_should_not_have_empty_title(self):
        def exam_with_empty_title():
            return ExamCreate(title='', questions=[QuestionExample().build()])

        self.assertRaises(ValidationError, exam_with_empty_title)

    def test_exam_should_not_have_empty_questions(self):
        def exam_without_questions():
            return ExamCreate(title='title', questions=[])

        self.assertRaises(ValidationError, exam_without_questions)


if __name__ == '__main__':
    unittest.main()
