from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.db import crud
from app.dependencies import get_db

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_courses(db, skip=skip, limit=limit)


@router.post("", status_code=201, response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)
