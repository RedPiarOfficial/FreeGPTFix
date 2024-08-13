class XwpNonceError(Exception):
    """Exception raised for errors related to x-wp-nonce generation."""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f'Error generating x-wp-nonce: {self.args[0]}. Please contact @Redpiar.'


class SessionIDError(Exception):
    """Exception raised for errors related to SessionID generation."""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f'Error generating SessionID: {self.args[0]}. Please contact @Redpiar.'


class CookiesError(Exception):
    """Exception raised for errors related to cookie generation."""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f'Error generating Cookie: {self.args[0]}. Please contact @Redpiar.'