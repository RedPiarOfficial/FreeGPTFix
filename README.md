# FreeGPTFix

<img src="https://repository-images.githubusercontent.com/636250478/f62a1186-b84b-4e7a-86f1-145e32163a59" align="right" width=170>

![Status](https://img.shields.io/pypi/status/freeGPT)

Version: 1.0.1

Author: RedPiar

freeGPT provides free access to text and image generation models.

# Contents

1. [Description](#desc)
2. [Models](#sources)
3. [Examples](#examples)
   1. [TextGen](#completion)
   2. [ImageGen](#generation)

## Getting Started:

    pip install freeGPTFix

## Sources:

| Model        | Website                                                |
| ------------ | ------------------------------------------------------ |
| gpt3         | [chat9.yqcloud.top](https://chat9.yqcloud.top/)        |
| gpt4         | [you.com](https://you.com/)                            |
| gpt3_5       | [vitalentum.net](https://vitalentum.net/free-chat-gpt) |
| prodia       | [prodia.com](https://prodia.com/)                      |
| pollinations | [pollinations.ai](https://pollinations.ai/)            |

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
