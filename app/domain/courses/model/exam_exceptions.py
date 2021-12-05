class ExamError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(self.code, self.message)

    def __str__(self):
        return self.message


class ExamsNotFoundError(ExamError):
    def __init__(self, course_id: int):
        super(ExamsNotFoundError, self).__init__('EXAMS_NOT_FOUND', f'No exams found for course {course_id}')
