from typing import List

import requests


class SubscriptionsService:
    host = 'https://ubademy-subscriptions-api.herokuapp.com'

    def get_subscriptions(self) -> List[str]:
        url = "{}/subscriptions".format(self.host)

        response = requests.get(url)
        subscriptions = response.json()

        return [subscription['code'] for subscription in subscriptions]
