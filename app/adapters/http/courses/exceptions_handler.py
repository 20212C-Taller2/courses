from fastapi import status, Request
from starlette.responses import JSONResponse

from app.domain.courses.model.course_exceptions import CourseNotFoundError


async def course_not_found_exception_handler(
        _request: Request, exc: CourseNotFoundError
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": exc.message})
