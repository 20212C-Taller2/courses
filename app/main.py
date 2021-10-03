from fastapi import FastAPI

from app.db import models
from app.db.database import engine
from app.routers import items

models.BaseModelDb.metadata.create_all(bind=engine)  # Replace with alembic

app = FastAPI()
app.include_router(items.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
