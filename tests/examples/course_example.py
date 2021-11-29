from app.domain.courses.model.course_type import CourseType
from app.domain.courses.model.courses import CourseCreate


class CourseExample(object):
    def __init__(self):
        self.title = 'title'
        self.description = 'description'
        self.exams = 1
        self.subscription = 'FREE'
        self.type = CourseType.WEB_DEVELOPMENT
        self.creator = 'profe@domain.com'
        self.location = None
        self.tags = set()
        self.media = set()

    def build(self):
        return CourseCreate(title=self.title, description=self.description, exams=self.exams,
                            subscription=self.subscription, type=self.type, creator=self.creator,
                            location=self.location, tags=self.tags, media=self.media)

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

    def with_tags(self, value):
        self.tags = set(value)
        return self

    def with_media(self, value):
        self.media = set(value)
        return self
