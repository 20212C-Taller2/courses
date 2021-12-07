import unittest

from pydantic import ValidationError

from app.domain.exams.questions import Question


class TestQuestionUseCase(unittest.TestCase):
    def test_question_attributes(self):
        question = Question(number=1, text='question')

        self.assertIsInstance(question.number, int)
        self.assertIsInstance(question.text, str)

    def test_question_number_should_be_greater_than_zero(self):
        def question_number_not_positive(number: int):
            Question(number=number, text='question')

        self.assertRaises(ValidationError, question_number_not_positive, 0)
        self.assertRaises(ValidationError, question_number_not_positive, -1)

    def test_question_title_should_not_be_empty(self):
        def question_title_empty():
            Question(number=1, text='')

        self.assertRaises(ValidationError, question_title_empty)


if __name__ == '__main__':
    unittest.main()
