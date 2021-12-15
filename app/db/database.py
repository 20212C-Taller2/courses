from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.conf.config import Settings, settings


def get_database_url(uri: str) -> str:
    if uri.startswith("postgres://"):
        return uri.replace("postgres://", "postgresql://", 1)
    return uri


engine = create_engine(
    get_database_url(settings.DATABASE_URL)
)
def get_session_factory():
    return sessionmaker(bind=engine, autocommit=False, autoflush=False)


BaseModelDb = declarative_base()
