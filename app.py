# app.py

from flask import Flask, render_template, request, jsonify
from core.engine import generate_template
from templates_registry.template_registry import TEMPLATES

app = Flask(__name__)


def get_templates_for_frontend():
    grouped = {}

    for key, data in TEMPLATES.items():
        category = data["category"]

        grouped.setdefault(category, {})

        grouped[category][key] = {
            "label": data["label"],
            "fields": data["fields"]
        }

    return grouped


@app.route("/")
def home():
    return render_template(
        "index.html",
        templates=get_templates_for_frontend()
    )


@app.route("/generate", methods=["POST"])
def generate():

    if not request.is_json:
        return jsonify({"error": "Formato inválido. Se esperaba JSON."}), 400

    data = request.get_json()

    template_key = data.get("template_key")
    form_data = data.get("form_data")

    if not template_key:
        return jsonify({"error": "No se envió template_key"}), 400

    if not isinstance(form_data, dict):
        return jsonify({"error": "form_data inválido"}), 400

    try:
        result = generate_template(template_key, form_data)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
