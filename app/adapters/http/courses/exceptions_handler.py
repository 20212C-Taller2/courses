from fastapi import status, Request
from starlette.responses import JSONResponse

from app.domain.courses.course_exceptions import CourseError
from app.domain.courses.enrollment_exceptions import EnrollmentError
from app.domain.courses.subscription_exceptions import SubscriptionError
from app.domain.courses.user_exceptions import UserError
from app.domain.exams.exam_exceptions import ExamError
from app.ports.logger import logger


async def exam_error_exception_handler(
        _request: Request, exc: ExamError
) -> JSONResponse:
    logger.error(f'ExamError: {exc.__str__()}')
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=exc.__dict__)


async def course_error_exception_handler(
        _request: Request, exc: CourseError
) -> JSONResponse:
    logger.error(f'CourseError: {exc.__str__()}')
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=exc.__dict__)


async def subscription_error_exception_handler(
        _request: Request, exc: SubscriptionError
) -> JSONResponse:
    logger.error(f'SubscriptionError: {exc.__str__()}')
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=exc.__dict__)


async def user_error_exception_handler(
        _request: Request, exc: UserError
) -> JSONResponse:
    logger.error(f'UserError: {exc.__str__()}')
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.__dict__)


async def enrollment_error_exception_handler(
        _request: Request, exc: EnrollmentError
) -> JSONResponse:
    logger.error(f'EnrollmentError: {exc.__str__()}')
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content=exc.__dict__)
