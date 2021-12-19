from pydantic import BaseSettings


class Settings(BaseSettings):
    VERSION: str = '1.0.0'
    LOG_LEVEL: str
    DATABASE_URL: str
    HOST_SUBSCRIPTIONS_API: str
    HOST_USERS_API: str

    class Config:
        env_file = ".env"


settings = Settings()
