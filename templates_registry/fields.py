# templates_registry/fields.py

def text_field(name, label):
    return {
        "name": name,
        "label": label,
        "type": "text"
    }

def combo_field(name, label, options):
    return {
        "name": name,
        "label": label,
        "type": "combo",
        "options": options
    }
