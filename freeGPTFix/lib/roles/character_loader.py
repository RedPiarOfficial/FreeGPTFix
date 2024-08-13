import importlib
import os

def load_characters_from_directory(directory_path):
    characters = {}
    if not os.path.isdir(directory_path):
        print(f"Directory not found: {directory_path}")
        return characters

    for filename in os.listdir(directory_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove the .py extension
            module_path = f"{directory_path.replace('/', '.')}.{module_name}"
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, 'PROMPT'):
                    characters[module_name] = getattr(module, 'PROMPT')
            except ImportError as e:
                print(f"Error importing {module_path}: {e}")
    return characters
