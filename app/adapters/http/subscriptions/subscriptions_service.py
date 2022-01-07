from typing import List

import requests
from requests import HTTPError

from app.dependencies import get_settings
from app.domain.courses.courses import Course
from app.domain.courses.subscription_exceptions import StudentHasNoAvailableSubscriptionError
from app.ports.logger import logger


class SubscriptionsService:
    host = get_settings().HOST_SUBSCRIPTIONS_API
    NO_ACTIVE_SUBSCRIPTION_DETAIL = 'No active subscription'

    def get_subscriptions(self) -> List[str]:
        url = f"{self.host}/subscriptions"

        response = requests.get(url)
        subscriptions = response.json()

        return [subscription['code'] for subscription in subscriptions]

    def create_subscription_for_course(self, course: Course):
        if course.subscription != 'FREE':
            url = f"{self.host}/courses"

            body = {
                "course_id": str(course.id),
                "owner_id": course.creator,
                "subscription_code": course.subscription
            }

            response = requests.post(url, json=body)
            response.raise_for_status()

            logger.info(
                f'Suscripción {course.subscription} creada para usuario {course.creator} por el curso {course.id}')
            return response.json()

    def subscribe_student(self, course: Course, student_id: str):
        try:
            if course.subscription != 'FREE':
                url = f"{self.host}/courses/{course.id}/subscribeStudent"

                body = {
                    "subscriber_id": student_id
                }

                response = requests.post(url, json=body)
                response.raise_for_status()

                logger.info(f'Inscripción del estudiante {student_id} al curso {course.id} enviada')
                return response.json()
        except HTTPError as http_err:
            response_body = http_err.response.json()
            logger.error(f'HTTPError: {http_err.__str__()} {response_body}')

            if response_body['detail'] == self.NO_ACTIVE_SUBSCRIPTION_DETAIL:
                raise StudentHasNoAvailableSubscriptionError(course.subscription)
            raise http_err

    def unsubscribe_student(self, course: Course, student_id: str):
        if course.subscription != 'FREE':
            url = f"{self.host}/courses/{course.id}/subscribeStudent/{student_id}"

            response = requests.delete(url)
            response.raise_for_status()

            logger.info(f'Desinscripción del estudiante {student_id} al curso {course.id} enviada')


def get_subscriptions_service() -> SubscriptionsService:
    return SubscriptionsService()
