import subprocess

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.adapters.http.courses import courses_controller, exams_controller
from app.adapters.http.courses.exceptions_handler import course_error_exception_handler, \
    subscription_error_exception_handler, exam_error_exception_handler, user_error_exception_handler
from app.dependencies import get_settings
from app.domain.courses.course_exceptions import CourseError
from app.domain.courses.subscription_exceptions import SubscriptionError
from app.domain.courses.user_exceptions import UserError
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
    version=get_settings().VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exams_controller.router)
app.include_router(courses_controller.router)

app.add_exception_handler(ExamError, exam_error_exception_handler)
app.add_exception_handler(CourseError, course_error_exception_handler)
app.add_exception_handler(SubscriptionError, subscription_error_exception_handler)
app.add_exception_handler(UserError, user_error_exception_handler)
