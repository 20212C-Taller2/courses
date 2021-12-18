import requests

from app.dependencies import get_settings
from app.domain.courses.user_exceptions import UserNotFoundError
from app.ports.logger import logger


class UsersService:
    def __init__(self, token: str):
        self.host = get_settings().HOST_USERS_API
        self.token = token

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

    def get_user_by_id(self, user_id: str) -> str:
        url = f"{self.host}/users/{user_id}"

        response = requests.get(url,
                                headers={'authorization': f'Bearer {self.token}'}
                                )
        if response.ok:
            user = response.json()

            return user['id']
        else:
            logger.error(f'Error {response.status_code} invocando Users API {response.json()}')
            raise UserNotFoundError(user_id)


def get_users_service(token: str) -> UsersService:
    return UsersService(token)
