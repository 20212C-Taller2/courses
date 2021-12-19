class SubscriptionError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(self.code, self.message)

    def __str__(self):
        return self.message


class SubscriptionNotFoundError(SubscriptionError):
    def __init__(self, name: str):
        super(SubscriptionNotFoundError, self).__init__('SUBSCRIPTION_NOT_FOUND', f'Subscription {name} not found')


class SubscriptionCreationError(SubscriptionError):
    def __init__(self):
        super(SubscriptionCreationError, self).__init__('SUBSCRIPTION_CREATION_ERROR',
                                                        'Subscription for course cannot be created')
