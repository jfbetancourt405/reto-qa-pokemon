from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Schema mínimo para validar la respuesta de /pokemon/{pokemon}
pokemon_schema = {
    "type": "object",
    "required": ["id", "name", "abilities", "moves", "stats"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string"},
        "abilities": {
            "type": "array",
            "items": {"type": "object"}
        },
        "moves": {
            "type": "array",
            "items": {"type": "object"}
        },
        "stats": {
            "type": "array",
            "items": {"type": "object"}
        }
    },
    "additionalProperties": True
}

def validate_schema(name: str, data: dict):
    """
    Valida 'data' según el schema identificado por 'name'.
    Lanza jsonschema.exceptions.ValidationError si falla.
    """
    if name == "pokemon":
        try:
            validate(instance=data, schema=pokemon_schema)
        except ValidationError as e:
            # Re-lanzar con un mensaje más claro
            raise ValidationError(f"Schema 'pokemon' inválido: {e.message}")
    else:
        raise ValueError(f"Schema desconocido: {name}")
