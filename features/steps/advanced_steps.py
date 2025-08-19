from behave import then
from utils.http_client import get

@then('cada nombre en "{var_name}" existe en el endpoint pokemon')
def step_validate_names_exist(context, var_name):
    """
    Para cada nombre guardado en context.<var_name>,
    hace un GET a /pokemon/{name} y valida que el status sea 200.
    """
    names = getattr(context, var_name, [])
    assert isinstance(names, list), f'"{var_name}" no es una lista'

    for name in names:
        resp = get(f"pokemon/{name}")
        assert resp.status_code == 200, f'El Pokémon "{name}" no existe o falló con {resp.status_code}'
