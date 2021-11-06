from app.domain.courses.model.subscription import Subscription
from app.domain.courses.model.courses import CourseCreate


class CourseExample(object):
    def __init__(self):
        self.title = 'title'
        self.description = 'description'
        self.exams = 1
        self.subscription = Subscription.FREE
        self.type = 'WEB_DEV'

    def build(self):
        return CourseCreate(title=self.title, description=self.description, exams=self.exams,
                            subscription=self.subscription, type=self.type)

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

    def with_type(self, value):
        self.type = value
        return self