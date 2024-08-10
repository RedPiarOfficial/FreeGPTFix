import requests

class Proxy:
	def __init__(self, http_proxy=None, https_proxy=None):
		self.set_proxies(http_proxy, https_proxy)

	def set_proxies(self, http_proxy=None, https_proxy=None):
		self.proxies = {
			"http": http_proxy,
			"https": https_proxy
		}

	def post(self, url, headers=None, **kwargs):
		return requests.post(url, headers=headers, proxies=self.proxies, **kwargs)

	def get(self, url, headers=None, **kwargs):
		return requests.get(url, headers=headers, proxies=self.proxies, **kwargs)

proxy = Proxy()