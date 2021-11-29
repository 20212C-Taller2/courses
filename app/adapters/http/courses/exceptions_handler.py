from fastapi import status, Request
from starlette.responses import JSONResponse

from app.domain.courses.model.course_exceptions import CourseError
from app.domain.courses.model.subscription_exceptions import SubscriptionError


async def course_not_found_exception_handler(
        _request: Request, exc: CourseError
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": exc.message})


async def subscription_not_found_exception_handler(
        _request: Request, exc: SubscriptionError
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"message": exc.message})
