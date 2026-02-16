# templates_registry/constants.py

import json
import os

SETTINGS_FILE = "settings.json"


def get_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {
            "agent_name": "NOMBRE DE AGENTE",
            "agent_code": "CODIGO DE AGENTE"
        }

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_settings(data):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_author():
    s = get_settings()
    return f"{s['agent_name']} / {s['agent_code']}"
