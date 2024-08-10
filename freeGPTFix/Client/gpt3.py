"""
freeGPT's gpt3 module
"""

from requests import post
from requests.exceptions import RequestException
from ..lib.headers import GPT3_HEADERS
from ..lib.proxy import proxy
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
			resp = proxy.post(
				url="https://api.binjie.fun/api/generateStream",
				headers=GPT3_HEADERS,
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