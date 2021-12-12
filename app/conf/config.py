from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    HOST_SUBSCRIPTIONS_API: str

    class Config:
        env_file = ".env"


settings = Settings()
