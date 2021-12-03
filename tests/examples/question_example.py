from app.domain.courses.model.questions import Question


class QuestionExample(object):
    def __init__(self):
        self.number = 1
        self.text = 'question text'

    def build(self):
        return Question(number=self.number,
                        text=self.text)

    def with_number(self, number: int):
        self.number = number
        return self

    def with_text(self, text: str):
        self.text = text,
        return self
