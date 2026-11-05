# Exemplo "Voice" (TTS) do console xAI
import _env  # noqa: F401
import os
import requests

response = requests.post(
    f"https://{os.getenv('XAI_API_HOST', 'api.x.ai')}/v1/tts",
    headers={
        "Authorization": f"Bearer {os.environ['XAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={
        "text": "Hello! Welcome to the Grok Text to Speech API.",
        "voice_id": os.getenv("XAI_TTS_VOICE", "eve"),
        "language": "en",
    },
)
response.raise_for_status()

with open("hello.mp3", "wb") as f:
    f.write(response.content)

print(f"Saved {len(response.content):,} bytes to hello.mp3")
