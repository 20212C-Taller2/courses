from typing import List

import requests
from app.conf.config import settings


class SubscriptionsService:
    host = settings.HOST_SUBSCRIPTIONS_API

    def get_subscriptions(self) -> List[str]:
        url = "{}/subscriptions".format(self.host)

        response = requests.get(url)
        subscriptions = response.json()

        return [subscription['code'] for subscription in subscriptions]
