import unittest

from app.domain.courses.model.subscription import Subscription
from pydantic import ValidationError

from app.schemas import CourseCreate
from tests.examples.course_example import CourseExample


class TestCourseUseCases(unittest.TestCase):
    def test_course_attributes(self):
        course = CourseExample().build()

        self.assertIsInstance(course.title, str)
        self.assertIsInstance(course.description, str)
        self.assertIsInstance(course.exams, int)
        self.assertIsInstance(course.subscription, Subscription)

    def test_course_title_should_not_have_empty_title(self):
        def course_without_title():
            return CourseExample().with_title('').build()

        self.assertRaises(ValidationError, course_without_title)

    def test_course_exams_should_not_be_negative(self):
        def course_with_negative_number_of_exams():
            CourseCreate(title='title', description='desc', exams=-1)

        self.assertRaises(ValidationError, course_with_negative_number_of_exams)
