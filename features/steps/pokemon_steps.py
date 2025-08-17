from behave import then
from json.decoder import JSONDecodeError
from utils.schemas import validate_schema

@then('la respuesta tarda menos de {seconds:f} segundos')
def step_impl_time(context, seconds):
    """
    Verifica que la respuesta llegue en menos del tiempo indicado.
    """
    resp = getattr(context, "response", None)
    assert resp is not None, "No se encontró 'response' en el contexto."
    elapsed = getattr(resp, "elapsed", None)
    assert elapsed is not None, "La respuesta no tiene información de tiempo."
    total = elapsed.total_seconds()
    assert total < seconds, f"Tiempo {total:.3f}s >= {seconds:.3f}s"

@then('el body cumple el schema "{schema_name}"')
def step_impl_schema(context, schema_name):
    """
    Verifica que el cuerpo JSON cumpla el schema indicado.
    """
    resp = getattr(context, "response", None)
    assert resp is not None, "No se encontró 'response' en el contexto."
    try:
        data = resp.json()
    except JSONDecodeError:
        raise AssertionError(f"El cuerpo no es JSON válido: {resp.text[:200]}")
    try:
        validate_schema(schema_name, data)
    except Exception as e:
        raise AssertionError(f"Schema '{schema_name}' inválido: {e}")

from behave import then
import json

@then('el campo "name" es igual a "{expected_name}"')
def step_impl(context, expected_name):
    data = context.response.json()
    assert data.get("name") == expected_name, f'Se esperaba name={expected_name} pero fue {data.get("name")}'

@then('el campo "abilities" es un arreglo no vacío')
def step_impl(context):
    data = context.response.json()
    assert isinstance(data.get("abilities"), list), "abilities no es una lista"
    assert len(data.get("abilities")) > 0, "abilities está vacío"

@then('el campo "moves" es un arreglo no vacío')
def step_impl(context):
    data = context.response.json()
    assert isinstance(data.get("moves"), list), "moves no es una lista"
    assert len(data.get("moves")) > 0, "moves está vacío"

@then('el campo "stats" es un arreglo no vacío')
def step_impl(context):
    data = context.response.json()
    assert isinstance(data.get("stats"), list), "stats no es una lista"
    assert len(data.get("stats")) > 0, "stats está vacío"
