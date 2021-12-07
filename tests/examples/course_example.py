from app.domain.courses.course_type import CourseType
from app.domain.courses.courses import Course


class CourseExample(object):
    def __init__(self):
        self.id = 1
        self.title = 'title'
        self.description = 'description'
        self.subscription = 'FREE'
        self.type = CourseType.WEB_DEVELOPMENT
        self.creator = 'profe@example.com'
        self.location = None
        self.tags = set()
        self.media = set()

    def build(self):
        return Course(id=self.id, title=self.title, description=self.description,
                      subscription=self.subscription, type=self.type, creator=self.creator,
                      location=self.location, tags=self.tags, media=self.media)

    def with_title(self, value):
        self.title = value
        return self

    def with_description(self, value):
        self.description = value
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
