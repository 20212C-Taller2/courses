from typing import List

import requests

from app.dependencies import get_settings
from app.domain.courses.courses import Course
from app.ports.logger import logger


class SubscriptionsService:
    host = get_settings().HOST_SUBSCRIPTIONS_API

    def get_subscriptions(self) -> List[str]:
        url = f"{self.host}/subscriptions"

        response = requests.get(url)
        subscriptions = response.json()

        return [subscription['code'] for subscription in subscriptions]

    def create_subscription_for_course(self, course: Course):
        url = f"{self.host}/courses"

        body = {
            "course_id": str(course.id),
            "owner_id": course.creator,
            "subscription_code": course.subscription
        }

        response = requests.post(url, json=body)
        response.raise_for_status()

        logger.info(
            f'Subscripción {course.subscription} creada para usuario {course.creator} por el curso {course.id}')
        return response.json()


def get_subscriptions_service() -> SubscriptionsService:
    return SubscriptionsService()
