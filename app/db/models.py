"""
Modelos para el ORM de la base de datos
"""

from sqlalchemy import Column, Integer, String
from app.db.database import BaseModelDb


class course(BaseModelDb):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
