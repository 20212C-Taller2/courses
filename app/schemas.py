"""
Estos son los "modelos" de pydantic que son usados por la api para validar
campos
"""
from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
