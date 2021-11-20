class CourseError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class CourseNotFoundError(CourseError):
    def __init__(self, course_id: int):
        super(CourseNotFoundError, self).__init__(f'Course {course_id} not found')


class CoursesNotFoundError(CourseError):
    def __init__(self):
        super(CoursesNotFoundError, self).__init__(f'Courses not found')
