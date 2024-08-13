class Models:
	def __init__(self):
		self._models_list = [
			"gpt3",
			"gpt3_5",
			"gpt4",
			"prodia",
			"pollinations"
		]
		self._models_dict = {
			"Text": self._get_text_models(),
			"Image": self._get_image_models()
		}

		self._Characters = [
		{
			"Underlale": ["SANS", "PAPYRUS", "GASTER", "ALPHIS"],
			"Hunter_X_Hunter": ["GON", "KILLUA", "MERUEM", "NETERO"],
			"KimetsuNoYaiba": ["RENGOKU"],
			"Other": ["FRIEND", "HISTORIAN", "PSYCHIATRIST"]
		}
		]

	@property
	def models_list(self):
		return self._models_list

	@property
	def models_dict(self):
		return self._models_dict

	@property
	def characters(self):
		return self._Characters

	@property
	def model_for_text(self):
		return self._models_dict["Text"]

	@property
	def model_for_image(self):
		return self._models_dict["Image"]

	def _get_text_models(self):
		return ["gpt3", "gpt3_5", "gpt4"]

	def _get_image_models(self):
		return ["prodia", "pollinations"]