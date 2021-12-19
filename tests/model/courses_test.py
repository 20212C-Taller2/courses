import unittest

from pydantic import ValidationError

from app.domain.courses.course_type import CourseType
from app.domain.courses.courses import CourseCreate
from app.domain.courses.enrollment_exceptions import CreatorEnrollmentError, CollaboratorEnrollmentError, \
    CreatorRegisterError, StudentRegisterError, StudentAlreadyEnrolledError, CollaboratorAlreadyRegisteredError
from tests.examples.course_example import CourseExample


class TestCourseUseCases(unittest.TestCase):
    def test_course_attributes(self):
        course = CourseExample().build()

        self.assertIsInstance(course.id, int)
        self.assertIsInstance(course.title, str)
        self.assertIsInstance(course.description, str)
        self.assertIsInstance(course.subscription, str)
        self.assertIsInstance(course.type, CourseType)
        self.assertIsInstance(course.creator, str)
        self.assertIsInstance(course.tags, set)
        self.assertIsInstance(course.media, set)
        self.assertIsInstance(course.students, set)
        self.assertIsInstance(course.collaborators, set)

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

    def test_course_should_allow_students_to_enroll(self):
        student = 'alumno@example.com'
        course = CourseExample().build()

        course.enroll_student(student)

        self.assertSetEqual(course.students, {student})

    def test_course_should_allow_collaborators_to_be_register(self):
        collaborator = 'collaborator@example.com'
        course = CourseExample().build()

        course.register_collaborator(collaborator)

        self.assertSetEqual(course.collaborators, {collaborator})

    def test_course_should_not_allow_creator_to_enroll_as_student(self):
        creator_id = 'creator@example.com'
        course = CourseExample().with_creator(creator_id).build()

        def enroll_creator_as_student():
            course.enroll_student(creator_id)

        self.assertRaises(CreatorEnrollmentError, enroll_creator_as_student)

    def test_course_should_not_allow_collaborator_to_enroll_as_student(self):
        collaborator_id = 'collaborator@example.com'
        course = CourseExample().build()
        course.register_collaborator(collaborator_id)

        def enroll_collaborator_as_student():
            course.enroll_student(collaborator_id)

        self.assertRaises(CollaboratorEnrollmentError, enroll_collaborator_as_student)

    def test_course_should_not_allow_creator_to_register_as_collaborator(self):
        creator_id = 'creator@example.com'
        course = CourseExample().with_creator(creator_id).build()

        def register_creator_as_collaborator():
            course.register_collaborator(creator_id)

        self.assertRaises(CreatorRegisterError, register_creator_as_collaborator)

    def test_course_should_not_allow_student_to_register_as_collaborator(self):
        student_id = 'student@example.com'
        course = CourseExample().build()
        course.enroll_student(student_id)

        def register_student_as_collaborator():
            course.register_collaborator(student_id)

        self.assertRaises(StudentRegisterError, register_student_as_collaborator)

    def test_course_should_not_allow_student_to_be_enrolled_twice(self):
        student = 'alumno@example.com'
        course = CourseExample().build()

        def enroll_student():
            course.enroll_student(student)

        enroll_student()
        self.assertRaises(StudentAlreadyEnrolledError, enroll_student)

    def test_course_should_not_allow_collaborator_to_be_enrolled_twice(self):
        collaborator = 'collaborator@example.com'
        course = CourseExample().build()

        def register_collaborator():
            course.register_collaborator(collaborator)

        register_collaborator()

        self.assertRaises(CollaboratorAlreadyRegisteredError, register_collaborator)
