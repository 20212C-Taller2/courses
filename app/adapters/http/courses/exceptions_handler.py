from fastapi import status, Request
from starlette.responses import JSONResponse

from app.domain.courses.course_exceptions import CourseError
from app.domain.courses.subscription_exceptions import SubscriptionError
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
