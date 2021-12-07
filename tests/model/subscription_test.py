import unittest
from unittest.mock import Mock

from app.domain.courses.subscription import Subscription
from app.domain.courses.subscription_exceptions import SubscriptionNotFoundError


class TestSubscription(unittest.TestCase):
    def test_subscription_free(self):
        subscription = Subscription(code='FREE')

        self.assertIsInstance(subscription.code, str)
        self.assertEqual(subscription.code, 'FREE')

    def test_invalid_subscription_not_in_subscriptions_should_raise(self):
        subscriptions_service = Mock()
        subscriptions_service.get_subscriptions.return_value = ['valid']

        def invalid_subscription():
            Subscription.exists(subscriptions_service, 'invalid')

        self.assertRaises(SubscriptionNotFoundError, invalid_subscription)
