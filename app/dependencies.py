from functools import lru_cache
from typing import Iterator

from sqlalchemy.orm import Session

from app.conf.config import Settings
from app.db.database import get_session_factory


@lru_cache()
def get_settings():
    return Settings()


def get_session() -> Iterator[Session]:
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()
