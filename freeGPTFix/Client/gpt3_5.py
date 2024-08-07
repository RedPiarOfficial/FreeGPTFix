"""
freeGPT's gpt3.5 module
"""

from requests import post
from requests.exceptions import RequestException
from uuid import uuid4

class Completion:
	"""
	This class provides methods for generating completions based on prompts.
	"""

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
				headers={"authority": "chatgpt5free.com",
					"path": "/wp-json/mwai-ui/v1/chats/submit",
					"scheme": "https",
					"accept": "*/*",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json",
					"cookie": "_ga=GA1.1.1164364256.1723035611; __gsas=ID=93ce1eeabe6a3665:T=1723035614:RT=1723035614:S=ALNI_Mau1GaFql56MGuxlIO5Yof9i8pI6g; mwai_session_id=66b36ffcc662a; __gads=ID=8d91d54792d96acd:T=1723035606:RT=1723036111:S=ALNI_MZCxKWpk6ZJUMznYW4bBfKuO_uN3Q; __gpi=UID=00000e877ca7d791:T=1723035606:RT=1723036111:S=ALNI_MbNN8EV4pRoai1NEQqccyo_RKFPGw; __eoi=ID=6cf36da3fa62ad5b:T=1723035606:RT=1723036111:S=AA-Afjbmu2Be1uiS8CL7W0zlmpaj; _ga_WQV20EPC74=GS1.1.1723035610.1.1.1723036199.0.0.0",
					"origin": "https://chatgpt5free.com",
					"referer": "https://chatgpt5free.com/chatgpt-5-free/",
					"sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
					"sec-ch-ua-mobile": "?0",
					"sec-ch-ua-platform": "Windows",
					"sec-fetch-dest": "empty",
					"sec-fetch-mode": "cors",
					"sec-fetch-site": "same-origin",
					"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
					"x-wp-nonce": "a901745329"
				},
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