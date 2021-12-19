from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from requests import HTTPError
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.adapters.database.courses import sql_course_repository
from app.adapters.http.subscriptions.subscriptions_service import SubscriptionsService, get_subscriptions_service
from app.adapters.http.users.users_service import UsersService, get_users_service
from app.dependencies import get_session
from app.domain.courses import courses
from app.domain.courses.course_type import CourseType
from app.domain.courses.subscription import Subscription
from app.domain.courses.subscription_exceptions import SubscriptionCreationError
from app.domain.courses.user import User
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
                 db: Session = Depends(get_session)):
    logger.info('Consultando cursos')
    return sql_course_repository.get_courses(db, type, subscription, creator, skip=skip, limit=limit)


security = HTTPBearer()


@router.post("", response_model=courses.Course, status_code=status.HTTP_201_CREATED)
def create_course(course: courses.CourseCreate, authorization: HTTPAuthorizationCredentials = Security(security),
                  db: Session = Depends(get_session),
                  subscriptions_service: SubscriptionsService = Depends(get_subscriptions_service),
                  # users_service: UsersService = Depends(get_users_service)
                  ):
    try:
        logger.info(f'Creación de nuevo curso por usuario {course.creator} con token {authorization}')
        logger.debug(f'Auth: {authorization}')

        users_service: UsersService = get_users_service(authorization.credentials)

        Subscription.exists(subscriptions_service, course.subscription)
        User.exists(users_service, course.creator)

        created_course = sql_course_repository.create_course(db=db, course=course)

        subscriptions_service.create_subscription_for_course(created_course)

        return created_course
    except HTTPError as httpErr:
        logger.error(f'HTTPError: {httpErr.__str__()} invocando Users API')
        sql_course_repository.delete_course(db=db, course=course)
        raise SubscriptionCreationError()


@router.get("/types", response_model=List[str], status_code=status.HTTP_200_OK)
def get_course_types():
    return [t.value for t in CourseType]


@router.get("/{course_id}", response_model=courses.Course, status_code=status.HTTP_200_OK)
def get_course(course_id: int, db: Session = Depends(get_session)):
    return sql_course_repository.get_course(db, course_id)


@router.patch("/{course_id}", response_model=courses.Course, status_code=status.HTTP_200_OK)
def edit_course(course_id: int, course: courses.CourseBase, db: Session = Depends(get_session)):
    # TODO: validar que solo lo haga el creador
    return sql_course_repository.update_course(db, course_id, course)


@router.post("/{course_id}/{role}/{user_id}", status_code=status.HTTP_201_CREATED)
def enroll_to_course(course_id: int, role: str, user_id: str, db: Session = Depends(get_session)):
    course = sql_course_repository.get_course(db, course_id)

    # TODO: validar existencia de usuario contra API Users

    if role == 'students':
        enrollment = course.enroll_student(user_id)
        return sql_course_repository.save_enrollment(db, enrollment)
    elif role == 'collaborators':
        course.register_collaborator(user_id)
        return sql_course_repository.save_collaborator(db, course_id, user_id)


@router.get("/{role}/{user_id}", response_model=List[courses.Course], status_code=status.HTTP_200_OK)
def get_courses_for_user_by_role(role: str, user_id: str, skip: int = 0, limit: int = 100,
                                 db: Session = Depends(get_session)):
    if role == 'students':
        return sql_course_repository.get_courses_for_student(db, user_id, skip, limit)
    elif role == 'collaborators':
        return sql_course_repository.get_courses_for_collaborator(db, user_id, skip, limit)


@router.delete("/{course_id}/students/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def leave_course(course_id: int, user_id: str, db: Session = Depends(get_session)):
    # TODO: validar que hayan pasado menos de un día de la fecha de inscripción
    sql_course_repository.delete_enrollment(db, course_id, user_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
