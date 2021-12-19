import unittest
from datetime import datetime

from app.domain.courses.enrollment import Enrollment
from tests.examples.course_example import CourseExample


class TestEnrollment(unittest.TestCase):
    def test_enrollment_attributes(self):
        course = CourseExample().build()

        enrollment = Enrollment(student_id='student@example.com', course_id=course.id)

        self.assertIsInstance(enrollment.student_id, str)
        self.assertIsInstance(enrollment.course_id, int)
        self.assertIsInstance(enrollment.date_time, datetime)

    def test_enrollment_date_time_should_be_setteable(self):
        course = CourseExample().build()
        set_date_time = datetime(2020, 5, 17)

        enrollment = Enrollment(student_id='student@example.com',
                                course_id=course.id,
                                date_time=set_date_time)

        self.assertEqual(enrollment.date_time, set_date_time)

    def test_enroll_a_student_to_a_course_should_return_enrollment(self):
        course = CourseExample().build()
        student = 'student@example.com'
        enrollment = course.enroll_student(student)

        self.assertIsInstance(enrollment, Enrollment)


if __name__ == '__main__':
    unittest.main()
