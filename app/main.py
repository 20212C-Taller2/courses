from fastapi import FastAPI

from app.adapters.http.courses.exceptions_handler import course_not_found_exception_handler
from app.db import models
from app.db.database import engine
from app.domain.courses.model.course_exceptions import CourseNotFoundError
from app.routers import courses

models.BaseModelDb.metadata.create_all(bind=engine)  # Replace with alembic

app = FastAPI()
app.include_router(courses.router)

app.add_exception_handler(CourseNotFoundError, course_not_found_exception_handler)
