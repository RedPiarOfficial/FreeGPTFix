import os
import importlib
import inspect
import sys

# Добавляем корневую директорию проекта в путь поиска модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def load_characters_from_directory(directory_path):
	characters = {}
	if not os.path.isdir(directory_path):
		print(f"Directory not found: {directory_path}")
		return characters

	# Путь от корневой директории до директории с модулями
	relative_path = os.path.relpath(directory_path, start=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
	# Преобразуем путь в формат Python для импорта
	module_prefix = f"{relative_path.replace(os.path.sep, '.')}"
	
	for filename in os.listdir(directory_path):
		if filename.endswith(".py") and filename != "__init__.py":
			module_name = filename[:-3]  # Remove the .py extension
			module_path = f"{module_prefix}.{module_name}"
			try:
				module = importlib.import_module(module_path)
				# Получаем все классы модуля
				classes = [cls for name, cls in inspect.getmembers(module, inspect.isclass)]
				if classes:
					# Предполагается, что самый первый класс — это тот, который нам нужен
					first_class = classes[0]
					characters[module_name] = first_class
			except ImportError as e:
				print(f"Error importing {module_path}: {e}")
			except Exception as e:
				print(f"Error processing module {module_path}: {e}")
	return characters



class Roles:
	def __init__(self):
		self.prompts = {}
		self.load_prompts()

	def load_prompts(self):
		# Определяем базовую директорию относительно текущего файла
		base_dir = os.path.dirname(os.path.abspath(__file__))
		
		# Определяем пути к директориям относительно базовой директории
		directories = [
			os.path.join(base_dir, 'Characters', 'Undertale'),
			os.path.join(base_dir, 'Characters', 'Other'),
			os.path.join(base_dir, 'Characters', 'Hunter_X_Hunter')
		]
		
		# Загружаем промпты из всех директорий
		for directory in directories:
			if os.path.isdir(directory):
				characters = load_characters_from_directory(directory)
				self.prompts.update(characters)
			else:
				print(f"Directory does not exist or is not a directory: {directory}")

	def get_role(self, role):
		role_upper = role.lower()
		
		if role_upper in self.prompts:
			return self.prompts[role_upper]
		else:
			return None

	def get_role_names(self):
		return list(self.prompts.keys())
