import requests
import re
import json
from .headers import ROOM_HEADERS
from ..Exceptions import SessionIDError, XwpNonceError, CookiesError
class session:
	def __init__(self):
		self.data = {"cookies": {}, "active": {}}
		try:
			del ROOM_HEADERS["x-wp-nonce"]
			del ROOM_HEADERS["cookie"]
		except:
			pass
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
	def create(self):
		if not self.CreateCookies():
			raise CookiesError
		if not self.CreateSessionID():
			raise SessionIDError
		if not self.activeSession():
			raise XwpNonceError

		return self.data

	def CreateSessionID(self):
		response2 = requests.post('https://chatgpt5free.com/')
		for cookie in response2.cookies:
			if cookie.name == "mwai_session_id":
				self.data["cookies"]["mwai_session_id"] = cookie.value
				return True
		return False

	def CreateCookies(self):
		response = requests.get(
			'https://partner.googleadservices.com/gampad/cookie.js?domain=chatgpt5free.com&client=partner-pub-2632145759680618&product=SAS&callback=__sasCookie',
			headers=self.headers
		)
		json_match = re.search(r'__sasCookie\((\{.*\})\);', response.text)
		if json_match:
			json_data = json_match.group(1)
			# Преобразование строки JSON в словарь Python
			data = json.loads(json_data)
			
			# Извлечение куки
			cookies = data.get('_cookies_', [])
			
			self.data["cookies"]["__gsas"] = cookies[0]['_value_']
			self.data["cookies"]["__gpi"] = cookies[1]['_value_']
			return True
		return False

	def activeSession(self):
		ROOM_HEADERS["cookie"] = '; '.join(f'{key}={value}' for key, value in self.data["cookies"].items())
		resp = requests.post("https://chatgpt5free.com/wp-json/mwai/v1/start_session", headers=ROOM_HEADERS)
		if resp.json().get("restNonce"):
			self.data["active"]["x-wp-nonce"] = resp.json().get("restNonce")
			ROOM_HEADERS["x-wp-nonce"] = resp.json().get("restNonce")
			return True
		else:
			return False