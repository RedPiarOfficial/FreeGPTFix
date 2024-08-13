import json
import time
from uuid import uuid4
from pathlib import Path
from requests import post
from requests.exceptions import RequestException

from .headers import ROOM_HEADERS
from .proxy import proxy
from .helper import session
from .roles import Roles
from ..Exceptions import XwpNonceError

class GPTHistoryModel:
	API_URL = "https://chatgpt5free.com/wp-json/mwai-ui/v1/chats/submit"

	def __init__(self):
		session().create()

	def create(self, history, prompt):
		payload = self._build_payload(history, prompt)
		try:
			response = proxy.post(self.API_URL, headers=ROOM_HEADERS, json=payload)
			response.raise_for_status()
			return response.json()
		except RequestException as exc:
			raise RequestException(f"Failed to fetch response: {exc}") from exc

	@staticmethod
	def _build_payload(history, prompt):
		return {
			"botId": "default",
			"customId": None,
			"session": "N/A",
			"chatId": str(uuid4()),
			"messages": history,
			"newMessage": prompt,
			"newFileId": None,
			"stream": False
		}

class Room:
	DEFAULT_HISTORY_FILE = "./history/history.json"
	INITIAL_MESSAGE = {
		"role": "assistant",
		"id": str(uuid4()),
		"timestamp": int(time.time()),
		"content": "Hi! How can I help you?",
		"who": "AI"
	}

	def __init__(self, history_path=None, role=None):
		self.history_path = history_path
		self.history = self._load_history(history_path) if history_path else self._initialize_history()
		self.temp_history = [self.INITIAL_MESSAGE.copy()]  # Ensure temp_history is initialized
		if role:
			self._setRole(self.history if self.history else self.temp_history, role)

	def start(self):
		# Ensure temp_history is initialized
		if not self.temp_history:
			self.temp_history = [self.INITIAL_MESSAGE.copy()]

	def send_message(self, text):
		history_to_use = self.history if self.history else self.temp_history
		model = GPTHistoryModel()
		response = model.create(history=history_to_use, prompt=text)
		self._append_message(history_to_use, "user", text)
		self._append_message(history_to_use, "assistant", response.get("reply", ""))
		return response

	def saveHistory(self, path=None):
		history_path = path or self.history_path or self.DEFAULT_HISTORY_FILE
		file_path = Path(history_path)
		file_path.parent.mkdir(parents=True, exist_ok=True)

		with open(file_path, 'w', encoding='utf-8') as file:
			json.dump(self.history if self.history else self.temp_history, file, indent=5, ensure_ascii=False)

	def get_history(self):
		return self.temp_history if not self.history else self.history

	def _load_history(self, path):
		try:
			with open(path, 'r', encoding='utf-8') as file:
				return json.load(file)
		except FileNotFoundError:
			return [self.INITIAL_MESSAGE.copy()]

	def _initialize_history(self):
		return [self.INITIAL_MESSAGE.copy()]

	def _setRole(self, historyObject, role):
		prompt = role().description()
		if prompt:
			historyObject.insert(0, {
				"role": "system",
				"id": str(uuid4()),
				"timestamp": int(time.time()),
				"content": prompt,
				"who": "system: "
			})

	@staticmethod
	def _append_message(history, role, content):
		history.append({
			"role": role,
			"id": str(uuid4()),
			"timestamp": int(time.time()),
			"content": content,
			"who": f"{role.capitalize()}: "
		})

	def __enter__(self):
		# Ensure temp_history is initialized
		self.start()
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		return False
