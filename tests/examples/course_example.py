from app.domain.courses.model.subscription import Subscription
from app.schemas import CourseCreate


class CourseExample(object):
    def __init__(self):
        self.title = 'title'
        self.description = 'description'
        self.exams = 1
        self.subscription = Subscription.FREE

    def build(self):
        return CourseCreate(title=self.title, description=self.description, exams=self.exams,
                            subscription=self.subscription)

    def with_title(self, value):
        self.title = value
        return self

    def with_description(self, value):
        self.description = value
        return self

    def with_exams(self, value):
        self.exams = value
        return self

    def with_subscription(self, value):
        self.subscription = value
        return self
