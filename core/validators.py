# core/validators.py

from templates_registry.template_registry import TEMPLATES


def clean_data(data: dict) -> dict:
    return {
        k: v.strip() if isinstance(v, str) else v
        for k, v in data.items()
    }


def validate_required_fields(template_key: str, data: dict):

    if template_key not in TEMPLATES:
        return False, "❌ Plantilla no registrada."

    required_fields = TEMPLATES[template_key]["fields"]

    for field in required_fields:
        name = field["name"]
        label = field["label"]

        if name not in data or not data[name]:
            return False, f"❌ Falta el campo requerido: {label}"

    return True, None
