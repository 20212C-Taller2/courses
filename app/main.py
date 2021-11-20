from fastapi import FastAPI

from app.adapters.database.courses import model
from app.adapters.http.courses import courses_controller
from app.adapters.http.courses.exceptions_handler import course_not_found_exception_handler
from app.db.database import engine
from app.domain.courses.model.course_exceptions import CourseError

model.BaseModelDb.metadata.create_all(bind=engine)  # Replace with alembic

app = FastAPI()
app.include_router(courses_controller.router)

app.add_exception_handler(CourseError, course_not_found_exception_handler)
