from app.domain.exams.answer import Answer
from tests.examples.question_example import QuestionExample


class AnswerExample:
    def __init__(self):
        self.question = QuestionExample().build()
        self.text = 'answer'

    def build(self):
        return Answer(question=self.question,
                      text=self.text)

    def with_question(self, question):
        self.question = question
        return self

    def with_answer(self, answer):
        self.text = answer
        return self
