from typing import List, Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.adapters.database.courses import sql_course_repository
from app.adapters.http.subscriptions.subscriptions_service import SubscriptionsService
from app.dependencies import get_db, get_subscriptions_service
from app.domain.courses import courses
from app.domain.courses.course_type import CourseType
from app.domain.courses.subscription import Subscription
from app.ports.logger import logger

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[courses.Course], status_code=status.HTTP_200_OK)
def read_courses(type: Optional[CourseType] = None, subscription: Optional[str] = None,
                 creator: Optional[str] = None, skip: int = 0, limit: int = 100,
                 db: Session = Depends(get_db)):
    logger.info(f'Consultando cursos')
    return sql_course_repository.get_courses(db, type, subscription, creator, skip=skip, limit=limit)


@router.post("", response_model=courses.Course, status_code=status.HTTP_201_CREATED)
def create_course(course: courses.CourseCreate, db: Session = Depends(get_db),
                  subscriptions_service: SubscriptionsService = Depends(get_subscriptions_service)):
    Subscription.exists(subscriptions_service, course.subscription)

    return sql_course_repository.create_course(db=db, course=course)


@router.get("/types", response_model=List[str], status_code=status.HTTP_200_OK)
def get_course_types():
    return [t.value for t in CourseType]


@router.get("/{course_id}", response_model=courses.Course, status_code=status.HTTP_200_OK)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return sql_course_repository.get_course(db, course_id)


@router.patch("/{course_id}", response_model=courses.Course, status_code=status.HTTP_200_OK)
def edit_course(course_id: int, course: courses.CourseBase, db: Session = Depends(get_db)):
    return sql_course_repository.update_course(db, course_id, course)


@router.post("/{course_id}/{role}/{user_id}", status_code=status.HTTP_201_CREATED)
def enroll_to_course(course_id: int, role: str, user_id: str, db: Session = Depends(get_db)):
    course = sql_course_repository.get_course(db, course_id)

    # TODO: validar existencia de usuario contra API Users

    if role == 'students':
        course.enroll_student(user_id)
        return sql_course_repository.save_enrollment(db, course_id, user_id)
    elif role == 'collaborators':
        course.register_collaborator(user_id)
        return sql_course_repository.save_collaborator(db, course_id, user_id)


@router.get("/{role}/{user_id}", response_model=List[courses.Course], status_code=status.HTTP_200_OK)
def get_courses_for_user_by_role(role: str, user_id: str, skip: int = 0, limit: int = 100,
                                 db: Session = Depends(get_db)):
    if role == 'students':
        return sql_course_repository.get_courses_for_student(db, user_id, skip, limit)
    elif role == 'collaborators':
        return sql_course_repository.get_courses_for_collaborator(db, user_id, skip, limit)


@router.delete("/{course_id}/students/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def leave_course(course_id: int, user_id: str, db: Session = Depends(get_db)):
    sql_course_repository.delete_enrollment(db, course_id, user_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
