from typing import Dict, Any

class Pokemon:
    REQUIRED_FIELDS = [
        "id",
        "name",
        "height",
        "weight",
        "abilities",
        "types"
    ]

    @staticmethod
    def validate_structure(data: Dict[str, Any]) -> bool:
        """
        Valida que el body de la respuesta contenga los campos requeridos
        y que cada campo tenga el tipo de dato correcto.
        """
        # Validar que sea un diccionario
        if not isinstance(data, dict):
            return False

        # Validar campos requeridos
        for field in Pokemon.REQUIRED_FIELDS:
            if field not in data:
                print(f"Falta el campo: {field}")
                return False

        # Validar tipos básicos
        if not isinstance(data["id"], int):
            return False
        if not isinstance(data["name"], str):
            return False
        if not isinstance(data["height"], int):
            return False
        if not isinstance(data["weight"], int):
            return False
        if not isinstance(data["abilities"], list):
            return False
        if not isinstance(data["types"], list):
            return False

        return True
