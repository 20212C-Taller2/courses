from fastapi import FastAPI

from app.db import models
from app.db.database import engine
from app.routers import courses

models.BaseModelDb.metadata.create_all(bind=engine)  # Replace with alembic

app = FastAPI()
app.include_router(courses.router)
