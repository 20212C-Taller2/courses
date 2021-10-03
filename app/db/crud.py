from sqlalchemy.orm import Session

from . import models
from .. import schemas

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.course).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course
