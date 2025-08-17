from utils.http_client import get  # importa nuestro cliente HTTP

@when('guardo los nombres de "{field}" de "{path}" como "{var_name}"')
def step_save_names(context, field, path, var_name):
    """
    Hace GET a la ruta dada, extrae el campo 'name' de cada elemento en 'field'
    y lo guarda en context.var_name para usarlo luego.
    """
    resp = get(path)  # usamos directamente nuestro cliente HTTP
    context.response = resp
    data = resp.json()
    results = data.get(field, [])
    names = [item.get("name", "") for item in results]
    setattr(context, var_name, names)
from behave import then

@then('la longitud de "{field}" es {expected_len:d}')
def step_check_length(context, field, expected_len):
    """
    Valida que el campo `field` en la respuesta tenga exactamente `expected_len` elementos.
    """
    data = context.response.json()
    items = data.get(field, [])
    assert isinstance(items, list), f'El campo "{field}" no es una lista'
    assert len(items) == expected_len, f'Se esperaban {expected_len} elementos en "{field}", pero se obtuvo {len(items)}'


@then('no hay elementos duplicados entre "{var1}" y "{var2}"')
def step_no_duplicates(context, var1, var2):
    """
    Valida que las listas guardadas en `context.var1` y `context.var2` no tengan elementos en común.
    """
    list1 = getattr(context, var1, [])
    list2 = getattr(context, var2, [])
    duplicates = set(list1) & set(list2)
    assert not duplicates, f'Se encontraron duplicados entre páginas: {duplicates}'


@then('el campo "{field}" es un número mayor que 0')
def step_field_greater_than_zero(context, field):
    """
    Valida que el campo `field` de la respuesta sea un número mayor a 0.
    """
    data = context.response.json()
    value = data.get(field, None)
    assert isinstance(value, int), f'El campo "{field}" no es un entero'
    assert value > 0, f'El campo "{field}" debería ser mayor que 0, pero es {value}'
