"""
freeGPT's gpt3.5 module
"""
from requests.exceptions import RequestException
from uuid import uuid4
from ..lib.headers import ROOM_HEADERS
from ..lib.proxy import proxy
from ..lib.helper import session
class Completion:
	def __init__(self):
		session().create()

	def create(self, prompt):
		try:
			res = proxy.post("https://chatgpt5free.com/wp-json/mwai-ui/v1/chats/submit",
				headers=ROOM_HEADERS,
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