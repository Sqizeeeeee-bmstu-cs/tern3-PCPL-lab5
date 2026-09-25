
class AccountBlockedException(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Account was blocked due to {self.message}"

class FraudException(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Transaction was aborted due to {self.message}"