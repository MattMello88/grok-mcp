# Exemplo "Image" do console xAI
import _env  # noqa: F401
import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"), api_host=os.getenv("XAI_API_HOST", "api.x.ai"))

response = client.image.sample(
    prompt="A collage of London landmarks in a stenciled street-art style",
    model=os.getenv("XAI_IMAGE_MODEL", "grok-imagine-image-2.0"),
)

print(response.url)
