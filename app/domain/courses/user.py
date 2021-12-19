from pydantic import BaseModel

from app.adapters.http.users.users_service import UsersService


class User(BaseModel):
    id: str

    @classmethod
    def exists(cls, users_service: UsersService, user_id: str) -> bool:
        User(id=users_service.get_user_by_id(user_id))
        return True
