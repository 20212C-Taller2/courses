import unittest

from pydantic import ValidationError

from app.domain.exams.answer import Answer
from app.domain.exams.questions import QuestionCreate
from tests.examples.question_example import QuestionExample


class TestAnswerUseCase(unittest.TestCase):
    def test_answer_attributes(self):
        answer = Answer(question=QuestionExample().build(),
                        text="question answer")

        self.assertIsInstance(answer.question, QuestionCreate)
        self.assertIsInstance(answer.text, str)

    def test_answer_should_not_have_empty_answer(self):
        def empty_answer():
            return Answer(question=QuestionExample().build(),
                          text="")

        self.assertRaises(ValidationError, empty_answer)


if __name__ == '__main__':
    unittest.main()
