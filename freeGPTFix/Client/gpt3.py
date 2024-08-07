"""
freeGPT's gpt3 module
"""

from requests import post
from requests.exceptions import RequestException


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
			resp = post(
				url="https://api.binjie.fun/api/generateStream",
				headers={
  "authority": "api.binjie.fun",
  "method": "POST",
  "path": "/api/generateStream",
  "scheme": "https",
  "accept": "application/json, text/plain, */*",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
  "content-type": "application/json",
  "origin": "https://chat18.aichatos8.com",
  "referer": "https://chat18.aichatos8.com/",
  "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "Windows",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "cross-site",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
},
				json={
					"prompt": prompt,
					"withoutContext": True,
					"stream": False,
				},
			)
			resp.encoding = "utf-8"
			return resp.text
		except RequestException as exc:
			raise RequestException("Unable to fetch the response.") from exc