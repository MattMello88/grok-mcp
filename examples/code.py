# Exemplo "Code" do console xAI
import _env  # noqa: F401
import os
from xai_sdk import Client
from xai_sdk.chat import user

client = Client(api_key=os.getenv("XAI_API_KEY"), api_host=os.getenv("XAI_API_HOST", "api.x.ai"))

chat = client.chat.create(model=os.getenv("XAI_CODE_MODEL", "grok-4.7"))
chat.append(user("Fix this function and explain the bug: function median(a){a.sort();return a[a.length/2]}"))

response = chat.sample()

print(response.content)
