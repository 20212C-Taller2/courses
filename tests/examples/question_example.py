from app.domain.exams.questions import Question


class QuestionExample(object):
    def __init__(self):
        self.id = 1
        self.number = 1
        self.text = 'question text'

    def build(self):
        return Question(id=self.id,
                        number=self.number,
                        text=self.text)

    def with_id(self, new_id: int):
        self.id = new_id
        return self

    def with_number(self, number: int):
        self.number = number
        return self

    def with_text(self, text: str):
        self.text = text
        return self
