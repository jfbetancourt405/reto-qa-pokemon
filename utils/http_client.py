import os
from typing import Optional, Dict, Any

import requests
from dotenv import load_dotenv

# Cargar variables de .env
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://pokeapi.co/api/v2")
TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "10"))

# Sesión HTTP reutilizable
_session = requests.Session()
_session.headers.update({
    "Accept": "application/json",
    "User-Agent": "qa-reto/1.0"
})

def _build_url(path: str) -> str:
    """Une BASE_URL con el path evitando dobles/malas barras."""
    return f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}"

def get(path: str, params: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None):
    """
    Realiza un GET a BASE_URL/path con params opcionales.
    No hace raise_for_status para permitir validar códigos no-200 en tests.
    """
    url = _build_url(path)
    resp = _session.get(url, params=params, timeout=timeout or TIMEOUT)
    return resp
