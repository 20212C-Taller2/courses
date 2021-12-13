from typing import List

import requests

from app.dependencies import get_settings


class SubscriptionsService:
    host = get_settings().HOST_SUBSCRIPTIONS_API

    def get_subscriptions(self) -> List[str]:
        url = "{}/subscriptions".format(self.host)

        response = requests.get(url)
        subscriptions = response.json()

        return [subscription['code'] for subscription in subscriptions]


def get_subscriptions_service() -> SubscriptionsService:
    return SubscriptionsService()
