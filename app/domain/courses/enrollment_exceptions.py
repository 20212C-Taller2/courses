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


class CreatorRegisterError(EnrollmentError):
    def __init__(self, user_id: str):
        super(CreatorRegisterError, self).__init__('ERROR_CREATOR_REGISTER',
                                                   f'Creator {user_id} cannot register as collaborator')


class StudentRegisterError(EnrollmentError):
    def __init__(self, user_id: str):
        super(StudentRegisterError, self).__init__('ERROR_STUDENT_REGISTER',
                                                   f'Student {user_id} cannot register as collaborator')


class StudentAlreadyEnrolledError(EnrollmentError):
    def __init__(self, user_id: str):
        super(StudentAlreadyEnrolledError, self).__init__('ERROR_STUDENT_ALREADY_ENROLLED',
                                                          f'Student {user_id} is already enrolled in this course')


class CollaboratorAlreadyRegisteredError(EnrollmentError):
    def __init__(self, user_id: str):
        super(CollaboratorAlreadyRegisteredError, self) \
            .__init__('ERROR_COLLABORATOR_ALREADY_ENROLLED',
                      f'Collaborator {user_id} is already registered in this course')


class UnenrollmentDateOverdueError(EnrollmentError):
    def __init__(self):
        super(UnenrollmentDateOverdueError, self).__init__('ERROR_UNENROLLMENT_DATE_OVERDUE',
                                                           'Cannot unenroll from course past one day from enrollment')
