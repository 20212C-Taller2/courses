import unittest

from app.domain.courses.model.subscription import Subscription


class TestSubscription(unittest.TestCase):
    def test_subscription_free(self):
        subscription = Subscription.FREE
        self.assertEqual(subscription.value, 'free')
