from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.adapters.database.courses import sql_course_repository
from app.dependencies import get_db
from app.domain.courses.model import courses
from app.domain.courses.model.course_type import CourseType
from app.domain.courses.model.subscription import Subscription

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[courses.Course], status_code=status.HTTP_200_OK)
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return sql_course_repository.get_courses(db, skip=skip, limit=limit)


@router.post("", response_model=courses.Course, status_code=status.HTTP_201_CREATED)
def create_course(course: courses.CourseCreate, db: Session = Depends(get_db)):
    return sql_course_repository.create_course(db=db, course=course)


@router.get("/subscriptions", response_model=List[str], status_code=status.HTTP_200_OK)
def get_subscriptions():
    return [s.value for s in Subscription]


@router.get("/types", response_model=List[str], status_code=status.HTTP_200_OK)
def get_course_types():
    return [t.value for t in CourseType]


@router.get("/{course_id}", response_model=courses.Course, status_code=status.HTTP_200_OK)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return sql_course_repository.get_course(db, course_id)
