import unittest

from app.domain.courses.model.course_type import CourseType


class TestCourseTypes(unittest.TestCase):
    def test_web_development_course_type(self):
        web_dev_course_type = CourseType.WEB_DEVELOPMENT
        self.assertEqual(web_dev_course_type.value, 'WEB_DEVELOPMENT')
