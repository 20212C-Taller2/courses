import requests

from app.dependencies import get_settings
from app.domain.courses.user_exceptions import UserNotFoundError
from app.ports.logger import logger


class UsersService:
    def __init__(self, token: str):
        self.host = get_settings().HOST_USERS_API
        self.token = token

    def get_user_by_id(self, user_id: str) -> str:
        url = f"{self.host}/users/{user_id}"

        response = requests.get(url,
                                headers={'authorization': f'Bearer {self.token}'}
                                )
        if response.ok:
            user = response.json()
            logger.info('Invocación a API Usuarios exitosa')

            return user['id']
        else:
            logger.error(f'Error {response.status_code} invocando Users API {response.json()}')
            raise UserNotFoundError(user_id)


def get_users_service(token: str) -> UsersService:
    return UsersService(token)
