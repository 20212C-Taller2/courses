from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.adapters.database.courses import model
from app.domain.courses.model import courses
from app.domain.courses.model.course_exceptions import CourseNotFoundError


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Course).offset(skip).limit(limit).all()


def create_course(db: Session, course: courses.CourseCreate):
    course_data = jsonable_encoder(course)
    db_course = model.Course(**course_data)

    db.add(db_course)

    db.commit()
    db.refresh(db_course)

    return db_course


def get_course(db: Session, course_id: int):
    course = db.query(model.Course).get(course_id)
    if not course:
        raise CourseNotFoundError(course_id)

    return course
