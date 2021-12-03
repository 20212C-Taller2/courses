import subprocess

from fastapi import FastAPI

from app.adapters.http.courses import courses_controller, exams_controller
from app.adapters.http.courses.exceptions_handler import course_not_found_exception_handler, \
    subscription_not_found_exception_handler
from app.domain.courses.model.course_exceptions import CourseError
from app.domain.courses.model.subscription_exceptions import SubscriptionError

# Perform db upgrade
subprocess.run(
    [
        "alembic",
        "upgrade",
        "head"
    ],
    stdout=subprocess.DEVNULL,
)

app = FastAPI(
    title="Courses API",
)
app.include_router(courses_controller.router)
app.include_router(exams_controller.router)

app.add_exception_handler(CourseError, course_not_found_exception_handler)
app.add_exception_handler(SubscriptionError, subscription_not_found_exception_handler)
