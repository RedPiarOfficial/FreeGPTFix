from ..lib.proxy import proxy
import json
import re
import random
import hashlib
import uuid

class Completion:
	def __init__(self):
		res = proxy.get(f"https://aichatonlineorg.erweima.ai/api/v1/user/getUniqueId?canvas={random.randint(1000000000, 9999999999)}")
		uniqueID = res.json()["data"]
		self.headers = {
		  "authority": "aichatonlineorg.erweima.ai",
		  "path": "/aichatonline/api/chat/gpt4o/chat",
		  "scheme": "https",
		  "accept": "*/*",
		  "accept-encoding": "gzip, deflate, br",
		  "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
		  "content-type": "application/json",
		  "origin": "https://aichatonline.org",
		  "referer": "https://aichatonline.org/",
		  "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
		  "sec-ch-ua-mobile": "?0",
		  "sec-ch-ua-platform": "\"Windows\"",
		  "sec-fetch-dest": "empty",
		  "sec-fetch-mode": "cors",
		  "sec-fetch-site": "cross-site",
		  "uniqueid": uniqueID,
		  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
		}

	def create(self, prompt):
		uuid_str = str(uuid.uuid4())
		# Создаем SHA-1 хеш от строки UUID
		hash_object = hashlib.sha1(uuid_str.encode())
		conversationId = hash_object.hexdigest()
		res = proxy.post("https://aichatonlineorg.erweima.ai/aichatonline/api/chat/gpt4o/chat",
							headers=self.headers,
							json={
								"attachments": [],
								"conversationId": conversationId,
								"prompt": prompt
							})

		data_str = res.text.strip()
		data = data_str.replace('"', "'")
		message_pattern = re.compile(r"'message':\s*'([^']*)'")
		messages = self.extract_pattern(data, message_pattern)
		# Объединение всех сообщений
		combined_message = ''.join(messages)

		# Извлечение текста после фигурных скобок
		if "{" in data:
			prompt = self.extract_content_between_braces(combined_message)
			message_after_braces = self.extract_text_after_braces(combined_message)

		
		# Извлечение URL
		urls = self.extract_url(data)

		# Составление результата
		result = {
			"prompt": prompt if prompt != '' else None,
			"urls": urls if urls != '' else None,
			"message": message_after_braces if message_after_braces != '' else combined_message
		}

		return result
	def extract_pattern(self, data_str, pattern):
		"""Извлекает данные, соответствующие шаблону, из строки."""
		return re.findall(pattern, data_str)

	def extract_content_between_braces(self,message):
		"""Извлекает текст между фигурными скобками из строки."""
		pattern = re.compile(r'\{(.*?)\}', re.DOTALL)
		match = pattern.search(message)
		return match.group(1).strip() if match else ""

	def extract_text_after_braces(self,message):
		"""Извлекает текст, идущий после закрывающей фигурной скобки."""
		pattern = re.compile(r'\}\s*(.*)', re.DOTALL)
		match = pattern.search(message)
		return match.group(1).strip() if match else ""

	def extract_url(self, data_str):
		"""Извлекает все URL из строки."""
		pattern = re.compile(r"'url':\s*'([^']*)'")
		return re.findall(pattern, data_str)