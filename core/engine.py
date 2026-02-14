# core/engine.py

from core.registry import GENERATORS
from core.validators import clean_data, validate_required_fields


def generate_template(template_key: str, data: dict) -> str:

    if template_key not in GENERATORS:
        return "❌ Plantilla no válida."

    cleaned_data = clean_data(data)

    is_valid, error = validate_required_fields(template_key, cleaned_data)

    if not is_valid:
        return error or "❌ Validación fallida."

    try:
        return GENERATORS[template_key](cleaned_data).strip()
    except Exception as e:
        return f"❌ Error al generar plantilla: {str(e)}"
