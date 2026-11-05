"""Funções reutilizáveis baseadas nos exemplos Python do console xAI."""
from __future__ import annotations

import time
from pathlib import Path

import requests
from xai_sdk import Client
from xai_sdk.chat import system, user

from . import config


def _require_key() -> str:
    if not config.XAI_API_KEY:
        raise RuntimeError("XAI_API_KEY não definida. Copie .env.example para .env e preencha a chave.")
    return config.XAI_API_KEY


def client() -> Client:
    return Client(api_key=_require_key(), api_host=config.XAI_API_HOST)


def chat(prompt: str, system_prompt: str | None = None, model: str | None = None) -> str:
    """Chat: equivalente ao exemplo 'Chat' do console."""
    c = client().chat.create(model=model or config.CHAT_MODEL)
    c.append(system(system_prompt or "You are Grok, a highly intelligent, helpful AI assistant."))
    c.append(user(prompt))
    return c.sample().content


def code(prompt: str, model: str | None = None) -> str:
    """Code: equivalente ao exemplo 'Code' do console (pedido de código sem system prompt)."""
    c = client().chat.create(model=model or config.CODE_MODEL)
    c.append(user(prompt))
    return c.sample().content


def image(prompt: str, model: str | None = None, aspect_ratio: str | None = None) -> str:
    """Image: gera uma imagem e retorna a URL."""
    kwargs = {"aspect_ratio": aspect_ratio} if aspect_ratio else {}
    resp = client().image.sample(prompt=prompt, model=model or config.IMAGE_MODEL, **kwargs)
    return resp.url


def video(
    prompt: str,
    model: str | None = None,
    duration: int = 10,
    aspect_ratio: str = "16:9",
    resolution: str = "720p",
) -> str:
    """Video: gera um vídeo (o SDK faz o polling) e retorna a URL."""
    resp = client().video.generate(
        prompt=prompt,
        model=model or config.VIDEO_MODEL,
        duration=duration,
        aspect_ratio=aspect_ratio,
        resolution=resolution,
    )
    return resp.url


def voice(
    text: str,
    voice_id: str | None = None,
    language: str | None = None,
    filename: str | None = None,
) -> Path:
    """Voice (TTS): converte texto em áudio mp3 e salva em OUTPUT_DIR."""
    response = requests.post(
        f"https://{config.XAI_API_HOST}/v1/tts",
        headers={"Authorization": f"Bearer {_require_key()}", "Content-Type": "application/json"},
        json={
            "text": text,
            "voice_id": voice_id or config.TTS_VOICE,
            "language": language or config.TTS_LANGUAGE,
        },
        timeout=120,
    )
    if response.status_code != 200:
        raise RuntimeError(f"TTS erro {response.status_code}: {response.text[:500]}")
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    name = Path(filename or f"tts-{int(time.time())}.mp3").name
    if not name.endswith(".mp3"):
        name += ".mp3"
    path = config.OUTPUT_DIR / name
    path.write_bytes(response.content)
    return path
