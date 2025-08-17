import os
from dotenv import load_dotenv

def before_all(context):
    """
    Hook que corre antes de todos los escenarios.
    Carga las variables de entorno y las guarda en el contexto.
    """
    load_dotenv()
    context.base_url = os.getenv("BASE_URL", "https://pokeapi.co/api/v2")
    context.request_timeout = float(os.getenv("REQUEST_TIMEOUT", "10"))
