# Exemplo "Video" do console xAI
import _env  # noqa: F401
import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"), api_host=os.getenv("XAI_API_HOST", "api.x.ai"))

response = client.video.generate(
    prompt="A glowing crystal-powered rocket launching from Mars",
    model=os.getenv("XAI_VIDEO_MODEL", "grok-imagine-video"),
    duration=10,
    aspect_ratio="16:9",
    resolution="720p",
)

print(response.url)
