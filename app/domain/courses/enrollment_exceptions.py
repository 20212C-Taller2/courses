class EnrollmentError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(self.code, self.message)

    def __str__(self):
        return self.message


class CreatorEnrollmentError(EnrollmentError):
    def __init__(self, user_id: str):
        super(CreatorEnrollmentError, self).__init__('ERROR_CREATOR_STUDENT_ENROLL',
                                                     f'Creator {user_id} cannot enroll as student')


class CollaboratorEnrollmentError(EnrollmentError):
    def __init__(self, user_id: str):
        super(CollaboratorEnrollmentError, self).__init__('ERROR_COLLABORATOR_STUDENT_ENROLL',
                                                          f'Collaborator {user_id} cannot enroll as student')
