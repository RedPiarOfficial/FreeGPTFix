# FreeGPTFix

<img src="https://repository-images.githubusercontent.com/636250478/f62a1186-b84b-4e7a-86f1-145e32163a59" align="right" width=170>

![Status](https://img.shields.io/pypi/status/freeGPT)

Version: 1.0.1

Author: RedPiar

freeGPT provides free access to text and image generation models.

# Contents

1. [Description](#description)
2. [Models](#sources)
3. [Examples](#examples)
   1. [TextGen](#completion)
   2. [ImageGen](#generation)
4. [Contacts](#contacts)

## Getting Started:

    pip install freeGPTFix

## description

This project is a direct fix for [FreeGPT](https://pypi.org/project/freeGPT/).
In [FreeGPT](https://pypi.org/project/freeGPT/), GPT-3 and GPT-3.5 do not work, and Python crashes with GPT-4, but it generates images correctly.
I also plan to improve this project and make it much better. An update will be released soon that will significantly distinguish [FreeGPTFix](https://github.com/RedPiarOfficial/FreeGPTFix) from [FreeGPT](https://pypi.org/project/freeGPT/).
## Sources:

| Model        | Website                                                | status       |
| ------------ | ------------------------------------------------------ | ------------ |
| gpt3         | [chat9.yqcloud.top](https://chat9.yqcloud.top/)        | :white_check_mark: |
| gpt4         | [you.com](https://you.com/)                            |  :white_check_mark: |
| gpt3_5       | [vitalentum.net](https://vitalentum.net/free-chat-gpt) | :white_check_mark: |
| prodia       | [prodia.com](https://prodia.com/)                      |  :white_check_mark: |
| pollinations | [pollinations.ai](https://pollinations.ai/)            | :white_check_mark: |

## Examples:

### Completion:

```python
from freeGPTFix import Client

while True:
    prompt = input("> ")
    try:
        resp = Client.create_completion("MODEL", prompt)
        print(resp)
    except Exception as e:
        print(f"🤖: {e}")
```

### Generation:

```python
from freeGPTFix import Client
from PIL import Image
from io import BytesIO

while True:
    prompt = input("> ")
    try:
        resp = Client.create_generation("MODEL", prompt)
        Image.open(BytesIO(resp)).show()
        print(f"🤖: Image shown.")
    except Exception as e:
        print(f"🤖: {e}")
```

# Contacts
| **Category**   | **Description** | **Link** |
|----------------|-----------------|----------|
| **My Contacts**|                 |          |
| Telegram       |                 | [Telegram](https://t.me/Redpiar) |
| TG Channel     |                 | [TG Channel](https://t.me/BotesForTelegram) |
| TikTok         |                 | [TikTok](https://www.tiktok.com/@redpiar) |
