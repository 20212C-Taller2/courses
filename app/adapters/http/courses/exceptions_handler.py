from fastapi import status, Request
from starlette.responses import JSONResponse

from app.domain.courses.model.course_exceptions import CourseError
from app.domain.courses.model.exam_exceptions import ExamError
from app.domain.courses.model.subscription_exceptions import SubscriptionError


async def exam_error_exception_handler(
        _request: Request, exc: ExamError
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=exc.__dict__)


async def course_error_exception_handler(
        _request: Request, exc: CourseError
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=exc.__dict__)


async def subscription_error_exception_handler(
        _request: Request, exc: SubscriptionError
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=exc.__dict__)
