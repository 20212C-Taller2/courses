from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.conf.config import Settings, settings


def get_database_url(env: Settings) -> str:
    uri = env.DATABASE_URL
    if uri.startswith("postgres://"):
        return uri.replace("postgres://", "postgresql://", 1)
    return uri


engine = create_engine(
    get_database_url(settings)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModelDb = declarative_base()
