"""Configuração lida do arquivo .env."""
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


def env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name)
    return value if value not in (None, "") else default


XAI_API_KEY = env("XAI_API_KEY")
XAI_API_HOST = env("XAI_API_HOST", "api.x.ai")
CHAT_MODEL = env("XAI_CHAT_MODEL", "grok-4.7")
CODE_MODEL = env("XAI_CODE_MODEL", "grok-4.7")
IMAGE_MODEL = env("XAI_IMAGE_MODEL", "grok-imagine-image-2.0")
VIDEO_MODEL = env("XAI_VIDEO_MODEL", "grok-imagine-video")
TTS_VOICE = env("XAI_TTS_VOICE", "eve")
TTS_LANGUAGE = env("XAI_TTS_LANGUAGE", "pt")
OUTPUT_DIR = Path(env("OUTPUT_DIR", str(ROOT / "output"))).expanduser()
if not OUTPUT_DIR.is_absolute():
    OUTPUT_DIR = (ROOT / OUTPUT_DIR).resolve()
