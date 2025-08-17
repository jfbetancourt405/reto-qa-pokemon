from behave import when, then
from utils.http_client import get

@when('hago GET a "{path}"')
def step_impl_get(context, path):
    """
    Envía un GET a la ruta especificada y guarda la respuesta en context.
    """
    context.response = get(path)

@then('la respuesta tiene status {code:d}')
def step_impl_status(context, code):
    """
    Valida el código de estado HTTP y muestra el body si falla.
    """
    assert hasattr(context, "response"), "No se encontró 'response' en el contexto"
    status = context.response.status_code
    if status != code:
        # Mostrar solo los primeros 800 caracteres del body para debug
        body_preview = context.response.text[:800]
        raise AssertionError(
            f"Esperado {code}, pero se recibió {status}.\nBody: {body_preview}"
        )

@then('el header "{name}" contiene "{valor}"')
def step_impl_header_contains(context, name, valor):
    """
    Verifica que el valor de un header contenga el texto esperado.
    """
    assert hasattr(context, "response"), "No se encontró 'response' en el contexto"
    header_value = context.response.headers.get(name, "")
    if valor not in header_value:
        raise AssertionError(
            f'El header "{name}" tiene valor "{header_value}", no contiene "{valor}"'
        )

@then('la respuesta tiene status 400 o 404')
def step_impl(context):
    assert context.response.status_code in [400, 404], \
        f"Esperado 400 o 404, pero se recibió {context.response.status_code}."
