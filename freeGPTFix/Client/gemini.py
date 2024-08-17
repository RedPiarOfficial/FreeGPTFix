#https://editee.com/chat-gpt

from ..lib.proxy import proxy
import random



class Completion:
	def __init__(self):
		self._sessionValue = self._getSession()
		self.headers = {
			"authority": "editee.com",
			"path": "/submit/chatgptfree",
			"scheme": "https",
			"accept": "application/json, text/plain, */*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
			"content-type": "application/json",
			"cookie": f"editeecom_session={self._sessionValue}",
			"origin": "https://editee.com",
			"referer": "https://editee.com/chat-gpt",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
			"x-requested-with": "XMLHttpRequest"
}

	def create(self, prompt):
		resp = proxy.post("https://editee.com/submit/chatgptfree",
							headers=self.headers, 
							json={
								f"context": " ",
								"selected_model": "gemini",
								"template_id": "",
								"user_input": prompt
					})

		return resp.json()

	def _getSession(self):
		res = proxy.get("https://editee.com/chat-gpt")
		if res.cookies.get_dict():
			first_cookie_name, self._editeecom_sessionValue = next(iter(res.cookies.get_dict().items()))
		return self._editeecom_sessionValue