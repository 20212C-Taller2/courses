from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.adapters.database.courses import model
from app.domain.courses.model import courses
from app.domain.courses.model.course_exceptions import CourseNotFoundError, CoursesNotFoundError
from app.domain.courses.model.course_type import CourseType
from app.domain.courses.model.courses import Course


def get_courses(db: Session, type: CourseType, subscription: str, creator: str, skip: int = 0, limit: int = 100):
    query = db.query(model.Course).order_by(model.Course.id)

    if type:
        query = query.filter(model.Course.type == type)

    if subscription:
        query = query.filter(model.Course.subscription == subscription)

    if creator:
        query = query.filter(model.Course.creator == creator)

    courses = query.offset(skip).limit(limit).all()

    if len(courses) == 0:
        raise CoursesNotFoundError()

    return [course.to_entity() for course in courses]


def create_course(db: Session, course: courses.CourseCreate):
    course_data = jsonable_encoder(course)
    db_course = model.Course(**course_data)

    db.add(db_course)

    db.commit()
    db.refresh(db_course)

    return db_course


def get_course(db: Session, course_id: int) -> Course:
    db_course = db.query(model.Course).get(course_id)
    if not db_course:
        raise CourseNotFoundError(course_id)

    return db_course.to_entity()


def update_course(db: Session, course_id: int, edited_course: courses.Course):
    db_course = db.query(model.Course).get(course_id)

    for var, value in vars(edited_course).items():
        setattr(db_course, var, value) if value else None

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return get_course(db, db_course.id)


def save_enrollment(db: Session, course_id: int, user_id: str):
    db_student = model.Student(id=user_id, course_id=course_id)

    db.add(db_student)

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_enrollment(db, course_id, user_id):
    enrollment = db.query(model.Student).get((user_id, course_id))

    db.delete(enrollment)
    db.commit()


def save_collaborator(db, course_id, user_id):
    db_collaborator = model.Collaborator(id=user_id, course_id=course_id)

    db.add(db_collaborator)

    db.commit()
    db.refresh(db_collaborator)

    return db_collaborator


def get_courses_for_student(db: Session, role: str, user_id: str, skip: int = 0, limit: int = 100):
    query = db.query(model.Student).join(model.Course.students).filter(model.Student.id == user_id)
    db_students = query.offset(skip).limit(limit).all()

    db_courses = [student.course for student in db_students]
    return [db_course.to_entity() for db_course in db_courses]


def get_courses_for_collaborator(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    query = db.query(model.Collaborator).join(model.Course.collaborators).filter(model.Collaborator.id == user_id)
    db_collaborators = query.offset(skip).limit(limit).all()

    db_courses = [collaborator.course for collaborator in db_collaborators]
    return [db_course.to_entity() for db_course in db_courses]
