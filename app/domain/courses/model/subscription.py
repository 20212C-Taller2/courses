from pydantic import BaseModel

from app.adapters.http.subscriptions.SubscriptionsService import SubscriptionsService
from app.domain.courses.model.subscription_exceptions import SubscriptionNotFoundError


class Subscription(BaseModel):
    code: str

    @classmethod
    def exists(cls, subscription_service: SubscriptionsService, subscription_name: str) -> None:
        subscriptions = [Subscription(code=name) for name in subscription_service.get_subscriptions()]

        found = next((sub for sub in subscriptions if sub.code == subscription_name), False)

        if not found:
            raise SubscriptionNotFoundError(subscription_name)
