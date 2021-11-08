import unittest

from pydantic import ValidationError

from app.domain.courses.model.course_type import CourseType
from app.domain.courses.model.courses import CourseCreate
from app.domain.courses.model.subscription import Subscription
from tests.examples.course_example import CourseExample


class TestCourseUseCases(unittest.TestCase):
    def test_course_attributes(self):
        course = CourseExample().build()

        self.assertIsInstance(course.title, str)
        self.assertIsInstance(course.description, str)
        self.assertIsInstance(course.exams, int)
        self.assertIsInstance(course.subscription, Subscription)
        self.assertIsInstance(course.type, CourseType)
        self.assertIsInstance(course.creator, str)
        self.assertIsInstance(course.tags, set)
        self.assertIsInstance(course.media, set)

    def test_course_title_should_not_have_empty_title(self):
        def course_without_title():
            return CourseExample().with_title('').build()

        self.assertRaises(ValidationError, course_without_title)

    def test_course_exams_should_not_be_negative(self):
        def course_with_negative_number_of_exams():
            CourseCreate(title='title', description='desc', exams=-1)

        self.assertRaises(ValidationError, course_with_negative_number_of_exams)

    def test_course_tags_could_be_empty(self):
        course = CourseExample().build()

        self.assertSetEqual(course.tags, set())

    def test_course_tags_should_be_a_set_of_names(self):
        tags = {'software', 'rest api'}
        course = CourseExample().with_tags(tags).build()

        self.assertSetEqual(course.tags, tags)

    def test_course_media_could_be_empty(self):
        course = CourseExample().build()

        self.assertSetEqual(course.media, set())

    def test_course_media_should_be_a_set_of_urls(self):
        paths = {'/path/to/file'}
        course = CourseExample().with_media(paths).build()

        self.assertSetEqual(course.media, paths)
