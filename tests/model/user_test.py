import unittest
from unittest import mock

from app.adapters.http.users.users_service import UsersService
from app.domain.courses.user import User
from app.domain.courses.user_exceptions import UserNotFoundError


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_body, status_code, ok):
            self.json_data = json_body
            self.status_code = status_code
            self.ok = ok

        def json(self):
            return self.json_data

    if '/valid_id' in args[0]:
        return MockResponse({"id": "valid_id"}, 200, True)

    return MockResponse({"message": f"There is no user with id: {args[0]}"}, 404, False)


class TestUsers(unittest.TestCase):
    def test_users(self):
        user = User(id='user_id')

        self.assertIsInstance(user.id, str)
        self.assertEqual(user.id, 'user_id')

    @mock.patch('app.adapters.http.users.users_service.requests.get', side_effect=mocked_requests_get)
    def test_existent_user_should_return_true(self, mock_get):
        users_service_mock = UsersService('fake_token')

        self.assertTrue(User.exists(users_service_mock, 'valid_id'))

    @mock.patch('app.adapters.http.users.users_service.requests.get', side_effect=mocked_requests_get)
    def test_inexistent_user_should_raise(self, mock_get):
        users_service_mock = UsersService('fake_token')

        def invalid_user():
            User.exists(users_service_mock, 'invalid_id')

        self.assertRaises(UserNotFoundError, invalid_user)
