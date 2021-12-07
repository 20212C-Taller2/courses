class CourseError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(self.code, self.message)

    def __str__(self):
        return self.message


class CourseNotFoundError(CourseError):
    def __init__(self, course_id: int):
        super(CourseNotFoundError, self).__init__('COURSE_NOT_FOUND', f'Course {course_id} not found')


class CoursesNotFoundError(CourseError):
    def __init__(self):
        super(CoursesNotFoundError, self).__init__('COURSES_NOT_FOUND', f'Courses not found')
