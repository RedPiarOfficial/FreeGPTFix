"""
freeGPT's gpt3.5 module
"""

from requests import post
from requests.exceptions import RequestException
from uuid import uuid4
from ..lib.headers import ROOM_HEADERS

class Completion:
	def __init__(self):
		self.ROOM_HEADERS = ROOM_HEADERS
		self.ROOM_HEADERS["x-wp-nonce"] = self.__GetSessionId__()

	def __GetSessionId__(self):
		resp = post("https://chatgpt5free.com/wp-json/mwai/v1/start_session", headers=self.ROOM_HEADERS)
		return resp.json().get("restNonce")

	def create(self, prompt):
		"""
		Create a completion for the given prompt using an AI text generation API.

		Args:
			prompt (str): The input prompt for generating the text.

		Returns:
			str: The generated text as a response from the API.

		Raises:
			requests.exceptions.RequestException: If there is an issue with sending the request or fetching the response.
		"""
		try:
			res = post("https://chatgpt5free.com/wp-json/mwai-ui/v1/chats/submit",
				headers=self.ROOM_HEADERS,
				json={
					"botId":"default",
					"customId":None,
					"session":"N/A",
					"chatId":str(uuid4()),
					"newMessage":prompt,
					"newFileId":None,
					"stream":False})
			return res.json()
		except RequestException as exc:
			raise RequestException("Unable to fetch the response.") from exc