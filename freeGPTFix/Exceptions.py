class XwpNonceError(Exception):
	def __init__(self):
		super().__init__()

	def __str__(self):
		return f'Error generating important component x-wp-nonce, please contact me: @Redpiar'

class SessionIDError(Exception):
	def __init__(self):
		super().__init__()

	def __str__(self):
		return f'Error generating important component SessionID, please contact me: @Redpiar'

class CookiesError(Exception):
	def __init__(self):
		super().__init__()

	def __str__(self):
		return f'Error generating important component Cookie, please contact me: @Redpiar'