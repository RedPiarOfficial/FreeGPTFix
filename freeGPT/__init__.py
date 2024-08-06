from freeGPT import *
import requests
__author__ = "RedPiar"
__Name__ = "donate"
__version__ = "1.0.0"

url = f"https://pypi.org/pypi/{__Name__}/json"
    
response = requests.get(url)
    
if response.status_code == 200:
    data = response.json()
        
    version = data['info']['version']
if version != __version__:
	print(f"Your version {__version__}, New version {version}")