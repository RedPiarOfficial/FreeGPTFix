from freeGPTFix import *
import requests
__author__ = "RedPiar"
__Name__ = "freeGPTFix"
__version__ = "1.0.5"

url = f"https://pypi.org/pypi/{__Name__}/json"
	
response = requests.get(url)
	
if response.status_code == 200:
	data = response.json()
		
	version = data['info']['version']
if version != __version__:
	print(f"[freeGPTFix] Your version {__version__}, New version {version}")