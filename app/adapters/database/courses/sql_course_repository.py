from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.adapters.database.courses import model
from app.domain.courses import courses
from app.domain.courses.course_exceptions import CourseNotFoundError, CoursesNotFoundError
from app.domain.courses.course_type import CourseType
from app.domain.courses.courses import Course
from app.domain.courses.enrollment import Enrollment


def get_courses(db: Session, type: CourseType, subscription: str, creator: str,
                skip: int = 0, limit: int = 100) -> List[Course]:
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


def update_course(db: Session, course_id: int, edited_course: courses.CourseBase):
    db_course = db.query(model.Course).get(course_id)

    for var, value in vars(edited_course).items():
        setattr(db_course, var, value) if value else None

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return get_course(db, db_course.id)


def save_enrollment(db: Session, enrollment: Enrollment):
    db_student = model.Student(student_id=enrollment.student_id,
                               course_id=enrollment.course_id,
                               enrollment_datetime=enrollment.date_time)

    db.add(db_student)

    db.commit()
    db.refresh(db_student)

    return db_student.to_entity()


def get_enrollment(db: Session, course_id: int, user_id: str) -> Enrollment:
    db_enrollment = db.query(model.Student).get((user_id, course_id))

    return db_enrollment.to_entity()


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


def get_courses_for_student(db: Session, user_id: str, skip: int = 0, limit: int = 100) -> List[Course]:
    query = db.query(model.Student) \
        .join(model.Course.students) \
        .filter(model.Student.student_id == user_id) \
        .order_by(model.Course.id)

    db_students = query.offset(skip).limit(limit).all()

    db_courses = [student.course for student in db_students]

    if len(db_courses) == 0:
        raise CoursesNotFoundError()

    return [db_course.to_entity() for db_course in db_courses]


def get_courses_for_collaborator(db: Session, user_id: str, skip: int = 0, limit: int = 100) -> List[Course]:
    query = db.query(model.Collaborator) \
        .join(model.Course.collaborators) \
        .filter(model.Collaborator.id == user_id) \
        .order_by(model.Course.id)

    db_collaborators = query.offset(skip).limit(limit).all()

    db_courses = [collaborator.course for collaborator in db_collaborators]

    if len(db_courses) == 0:
        raise CoursesNotFoundError()

    return [db_course.to_entity() for db_course in db_courses]


def delete_course(db, course: Course):
    db_course = db.query(model.Course).get(course.id)

    db.delete(db_course)
    db.commit()
