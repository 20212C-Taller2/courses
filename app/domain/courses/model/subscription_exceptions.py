class SubscriptionError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class SubscriptionNotFoundError(SubscriptionError):
    def __init__(self, name: str):
        super(SubscriptionNotFoundError, self).__init__(f'Subscription {name} not found')
