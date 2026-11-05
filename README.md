# grok-mcp

Servidor **MCP** para a API da xAI (Grok) com cinco ferramentas, baseadas nos exemplos Python do console xAI:

| Tool | O que faz |
|---|---|
| `grok_chat` | Conversa com o Grok (com system prompt opcional) |
| `grok_code` | Escreve, corrige e explica código |
| `grok_image` | Gera imagem (Grok Imagine) e retorna a URL |
| `grok_video` | Gera vídeo (Grok Imagine) e retorna a URL |
| `grok_voice` | Texto para fala — salva um `.mp3` em `OUTPUT_DIR` |

## Instalação (ex.: na pasta Herd)

```bash
cd ~/Herd
git clone https://github.com/MattMello88/grok-mcp.git
cd grok-mcp
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
cp .env.example .env             # Windows: copy .env.example .env
```

Edite o `.env` e preencha `XAI_API_KEY` (crie em console.x.ai › API Keys). Todas as variáveis ficam no `.env`.

## Exemplos avulsos

```bash
python examples/code.py
python examples/chat.py
python examples/image.py
python examples/video.py
python examples/voice.py
```

## Usando como MCP

### Claude Desktop / Claude Code (stdio)

```json
{
  "mcpServers": {
    "grok": {
      "command": "/caminho/para/Herd/grok-mcp/.venv/bin/grok-mcp"
    }
  }
}
```

No Windows use `C:\\Users\\voce\\Herd\\grok-mcp\\.venv\\Scripts\\grok-mcp.exe` (com barras duplas no JSON). Claude Code:

```bash
claude mcp add grok -- /caminho/para/Herd/grok-mcp/.venv/bin/grok-mcp
```

### HTTP (streamable-http)

No `.env`: `MCP_TRANSPORT=streamable-http`, `MCP_HOST`, `MCP_PORT`. Depois:

```bash
grok-mcp   # endpoint em http://127.0.0.1:8000/mcp
```

## Estrutura

```
grok_mcp/
  config.py   # lê o .env
  xai.py      # funções chat/code/image/video/voice
  server.py   # servidor MCP (tools)
examples/     # snippets Python do console xAI
```
