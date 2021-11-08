class CourseNotFoundError(Exception):
    def __init__(self, course_id: str):
        self.message = f'Course {course_id} not found'

    def __str__(self):
        return self.message
