import requests
from uuid import uuid4
from re import findall, sub

class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    def create(self, prompt):
        """
        Generate a completion based on the provided prompt.

        Args:
            prompt (str): The input prompt to generate a completion from.

        Returns:
            str: The generated completion as a text string.

        Raises:
            Exception: If the response does not contain the expected "youChatToken".
        """
        try:
            response = requests.get(
                "https://you.com/api/streamingSearch",
                headers={
                    "cache-control": "no-cache",
                    "referer": "https://you.com/search?q=gpt4&tbm=youchat",
                    "cookie": f"safesearch_guest=Off; uuid_guest={str(uuid4())}",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
                },
                params={
                    "q": prompt,
                    "page": 1,
                    "count": 10,
                    "safeSearch": "Off",
                    "onShoppingPage": False,
                    "mkt": "",
                    "responseFilter": "WebPages,Translations,TimeZone,Computation,RelatedSearches",
                    "domain": "youchat",
                    "queryTraceId": str(uuid4()),
                    "chat": [],
                },
            )
            if "youChatToken" not in response.text:
                raise Exception("Unable to fetch the response.")

            token = (
                "".join(
                    findall(
                        r"{\"youChatToken\": \"(.*?)\"}",
                        response.text
                    )
                )
                .replace("\\n", "\n")
                .replace("\\\\", "\\")
                .replace('\\"', '"')
            )
            decoded_string = token.encode('utf-8').decode('unicode_escape')
            text = sub(r'[#*]', '', decoded_string)
            return text
        
        except requests.RequestException as e:
            print("Request Error:", e)
            raise
        except Exception as e:
            print("General Error:", e)
            raise