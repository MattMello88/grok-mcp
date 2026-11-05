"""Carrega o .env da raiz do projeto para os exemplos."""
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
