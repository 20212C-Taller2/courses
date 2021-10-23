from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.dependencies import get_db

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[schemas.Course], status_code=status.HTTP_200_OK)
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_courses(db, skip=skip, limit=limit)


@router.post("", response_model=schemas.Course, status_code=status.HTTP_201_CREATED)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)


@router.get("/{course_id}", response_model=schemas.Course, status_code=status.HTTP_200_OK)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return crud.get_course(db, course_id)
