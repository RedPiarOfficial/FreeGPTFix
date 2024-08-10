from requests import post
from requests.exceptions import RequestException
from uuid import uuid4
from .headers import ROOM_HEADERS 
from .proxy import proxy
from ..Exceptions import XwpNonceError
import time
import json
import os
from pathlib import Path
from .helper import session
class GPTHistoryModel:
	def __init__(self):
		session().create()

	def create(self, history, prompt):
		try:
			res = proxy.post("https://chatgpt5free.com/wp-json/mwai-ui/v1/chats/submit",
				headers=ROOM_HEADERS,
				json={
					"botId":"default",
					"customId":None,
					"session": "N/A",
					"chatId":str(uuid4()),
					"messages": history,
					"newMessage":prompt,
					"newFileId":None,
					"stream":False})
			return res.json()
		except RequestException as exc:
			raise RequestException("Unable to fetch the response.") from exc

class Room:
	def __init__(self, history=None):
		self.historyPath = history
		self.history = history

		if self.history:
			self.__LoadHistory__(self.historyPath)
	def Start(self):
		self.tempHistory = [{"role": "assistant", "id": str(uuid4()), "timestamp":int(time.time()), "content": "Hi! How can i help you?","who": "AI: "}]
	def send_message(self, text):
		resp = GPTHistoryModel().create(history=self.history if self.history != None else self.tempHistory, prompt=text)
		if self.history:
			self.history.append({"role": "user", "id": str(uuid4()), "timestamp":int(time.time()), "content": text,"who": "User: "})
			self.history.append({"role": "assistant", "id": str(uuid4()), "timestamp":int(time.time()), "content": resp["reply"],"who": "AI: "})
		else:
			self.tempHistory.append({"role": "user", "id": str(uuid4()), "timestamp":int(time.time()), "content": text,"who": "User: "})
			self.tempHistory.append({"role": "assistant", "id": str(uuid4()), "timestamp":int(time.time()), "content": resp["reply"],"who": "AI: "})
		return resp

	def saveHistory(self, historyBPath = "./history/history.json"):
		if self.historyPath:
			historyBPath = self.historyPath
		file_path = Path(historyBPath)
		file_path.parent.mkdir(parents=True, exist_ok=True)
		with open(historyBPath, 'w', encoding='utf-8') as file:
			json.dump(self.history if self.history != None else self.tempHistory, file, indent=5, ensure_ascii=False)

	def getHistory(self):
		return self.tempHistory

	def __LoadHistory__(self, path):
		try:
			with open(path, "r", encoding='utf-8') as file:
				self.history = json.load(file)
		except FileNotFoundError:
			self.history = [{"role": "assistant", "id": str(uuid4()), "timestamp":int(time.time()), "content": "Hi! How can i help you?","who": "AI: "}]
	def __enter__(self):
		self.Start()
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		return False