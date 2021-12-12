import subprocess

from fastapi import FastAPI

from app.adapters.http.courses import courses_controller, exams_controller
from app.adapters.http.courses.exceptions_handler import course_error_exception_handler, \
    subscription_error_exception_handler, exam_error_exception_handler
from app.conf.config import settings
from app.domain.courses.course_exceptions import CourseError
from app.domain.courses.subscription_exceptions import SubscriptionError
from app.domain.exams.exam_exceptions import ExamError

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
    version=settings.VERSION
)

app.include_router(exams_controller.router)
app.include_router(courses_controller.router)

app.add_exception_handler(ExamError, exam_error_exception_handler)
app.add_exception_handler(CourseError, course_error_exception_handler)
app.add_exception_handler(SubscriptionError, subscription_error_exception_handler)
