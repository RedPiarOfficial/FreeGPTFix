import requests
import re
import json
from .headers import ROOM_HEADERS
from ..Exceptions import SessionIDError, XwpNonceError, CookiesError

class session:
	def __init__(self):
		self.data = {"cookies": {}, "active": {}}
		self._cleanup_headers()

		self.headers = {
			'authority': 'partner.googleadservices.com',
			'path': '/gampad/cookie.js?domain=chatgpt5free.com&client=partner-pub-2632145759680618&product=SAS&callback=__sasCookie',
			'scheme': 'https',
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
			'cookie': 'ar_debug=1; GCL_AW_P=GCL.1720684459.Cj0KCQjwhb60BhClARIsABGGtw_0wjNc43Pgn0mf6PiQbEnI237LTo3Xsifp5sn1816UBW_1XdKmYIIaAp9gEALw_wcB',
			'referer': 'https://chatgpt5free.com/',
			'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'script',
			'sec-fetch-mode': 'no-cors',
			'sec-fetch-site': 'cross-site',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
			'x-client-data': 'CI62yQEIpbbJAQipncoBCMeUywEIk6HLAQiFoM0B'
		}

	def _cleanup_headers(self):
		"""Remove specific keys from ROOM_HEADERS if they exist."""
		ROOM_HEADERS.pop("x-wp-nonce", None)
		ROOM_HEADERS.pop("cookie", None)
	def create(self):
		"""Creates a session with the necessary cookies and headers."""
		if not self._create_cookies():
			raise CookiesError("Failed to create cookies.")

		if not self._create_session_id():
			raise SessionIDError("Failed to create session ID.")

		if not self._activate_session():
			raise XwpNonceError("Failed to activate session.")

		return self.data

	def _create_session_id(self):
		"""Fetch the session ID and store it in self.data."""
		try:
			response = requests.post('https://chatgpt5free.com/')
			response.raise_for_status()
			for cookie in response.cookies:
				if cookie.name == "mwai_session_id":
					self.data["cookies"]["mwai_session_id"] = cookie.value
					return True
		except requests.RequestException as e:
			print(f"Error creating session ID: {e}")
		return False

	def _create_cookies(self):
		"""Fetch cookies from the external service and store them in self.data."""
		try:
			response = requests.get(
				'https://partner.googleadservices.com/gampad/cookie.js?domain=chatgpt5free.com&client=partner-pub-2632145759680618&product=SAS&callback=__sasCookie',
				headers=self.headers
			)
			response.raise_for_status()

			json_match = re.search(r'__sasCookie\((\{.*\})\);', response.text)
			if json_match:
				json_data = json_match.group(1)
				data = json.loads(json_data)

				cookies = data.get('_cookies_', [])
				if len(cookies) >= 2:
					self.data["cookies"]["__gsas"] = cookies[0]['_value_']
					self.data["cookies"]["__gpi"] = cookies[1]['_value_']
					return True
		except requests.RequestException as e:
			print(f"Error creating cookies: {e}")
		return False

	def _activate_session(self):
		"""Activate the session by sending the required headers."""
		try:
			ROOM_HEADERS["cookie"] = '; '.join(f'{key}={value}' for key, value in self.data["cookies"].items())
			response = requests.post("https://chatgpt5free.com/wp-json/mwai/v1/start_session", headers=ROOM_HEADERS)
			response.raise_for_status()

			nonce = response.json().get("restNonce")
			if nonce:
				self.data["active"]["x-wp-nonce"] = nonce
				ROOM_HEADERS["x-wp-nonce"] = nonce
				return True
		except requests.RequestException as e:
			print(f"Error activating session: {e}")
		return False

