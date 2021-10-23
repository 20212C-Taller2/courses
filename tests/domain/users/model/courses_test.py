import unittest

from pydantic import ValidationError

from app.schemas import CourseCreate


class TestCourseUseCases(unittest.TestCase):
    def test_course_attributes(self):
        course = CourseCreate(title='title', description='desc', exams=1)

        self.assertIsInstance(course.title, str)
        self.assertIsInstance(course.description, str)
        self.assertIsInstance(course.exams, int)

    def test_course_title_should_not_have_empty_title(self):
        def course_without_title():
            CourseCreate(title='', description='desc', exams=0)

        self.assertRaises(ValidationError, course_without_title)

    def test_course_title_should_not_have_empty_description(self):
        def course_without_description():
            CourseCreate(title='title', description='', exams=0)

        self.assertRaises(ValidationError, course_without_description)

    def test_course_exams_should_be_positive(self):
        def course_with_not_positive_number_of_exams():
            CourseCreate(title='title', description='desc', exams=-1)

        self.assertRaises(ValidationError, course_with_not_positive_number_of_exams)
