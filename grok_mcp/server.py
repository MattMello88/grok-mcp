"""Servidor MCP que expõe code, chat, imagem, vídeo e voz da API xAI (Grok)."""
from __future__ import annotations

from mcp.server.mcpserver import MCPServer

from . import config, xai

mcp = MCPServer(
    name="grok-mcp",
    version="0.1.0",
    instructions=(
        "Ferramentas da API xAI (Grok): grok_chat para conversa, grok_code para tarefas de código, "
        "grok_image para gerar imagens, grok_video para gerar vídeos e grok_voice para texto-para-fala. "
        "Imagem e vídeo retornam URLs; voz salva um mp3 em OUTPUT_DIR."
    ),
)


@mcp.tool()
def grok_chat(prompt: str, system_prompt: str | None = None, model: str | None = None) -> str:
    """Envia uma mensagem ao Grok e retorna a resposta em texto.

    Args:
        prompt: mensagem do usuário.
        system_prompt: instrução de sistema opcional.
        model: modelo (padrão XAI_CHAT_MODEL do .env).
    """
    return xai.chat(prompt, system_prompt=system_prompt, model=model)


@mcp.tool()
def grok_code(prompt: str, model: str | None = None) -> str:
    """Pede ao Grok para escrever, corrigir ou explicar código.

    Args:
        prompt: descrição da tarefa, incluindo o código quando for o caso.
        model: modelo (padrão XAI_CODE_MODEL do .env).
    """
    return xai.code(prompt, model=model)


@mcp.tool()
def grok_image(prompt: str, aspect_ratio: str | None = None, model: str | None = None) -> str:
    """Gera uma imagem com Grok Imagine e retorna a URL.

    Args:
        prompt: descrição da imagem.
        aspect_ratio: ex. "1:1", "16:9", "9:16" (opcional).
        model: modelo (padrão XAI_IMAGE_MODEL do .env).
    """
    return xai.image(prompt, model=model, aspect_ratio=aspect_ratio)


@mcp.tool()
def grok_video(
    prompt: str,
    duration: int = 10,
    aspect_ratio: str = "16:9",
    resolution: str = "720p",
    model: str | None = None,
) -> str:
    """Gera um vídeo com Grok Imagine (pode levar alguns minutos) e retorna a URL.

    Args:
        prompt: descrição do vídeo.
        duration: duração em segundos.
        aspect_ratio: "16:9", "9:16", "1:1", etc.
        resolution: "480p", "720p" ou "1080p".
        model: modelo (padrão XAI_VIDEO_MODEL do .env).
    """
    return xai.video(prompt, model=model, duration=duration, aspect_ratio=aspect_ratio, resolution=resolution)


@mcp.tool()
def grok_voice(
    text: str,
    voice_id: str | None = None,
    language: str | None = None,
    filename: str | None = None,
) -> str:
    """Converte texto em fala (mp3) e retorna o caminho do arquivo salvo.

    Args:
        text: texto a ser falado.
        voice_id: voz (padrão XAI_TTS_VOICE, ex. "eve").
        language: idioma (padrão XAI_TTS_LANGUAGE, ex. "pt", "en").
        filename: nome do arquivo mp3 (opcional).
    """
    path = xai.voice(text, voice_id=voice_id, language=language, filename=filename)
    return f"Áudio salvo em {path}"


def main() -> None:
    transport = config.env("MCP_TRANSPORT", "stdio")
    if transport == "stdio":
        mcp.run("stdio")
    else:
        mcp.run(transport, host=config.env("MCP_HOST", "127.0.0.1"), port=int(config.env("MCP_PORT", "8000")))


if __name__ == "__main__":
    main()
