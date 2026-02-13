from flask import Flask, render_template, request, jsonify
from core.generators import generate_template
from templates_registry.template_registry import TEMPLATES

app = Flask(__name__)


def get_templates_for_frontend():
    
    grouped = {}

    for key, data in TEMPLATES.items():
        category = data["category"]

        if category not in grouped:
            grouped[category] = {}

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

    data = request.json

    template_key = data.get("template_key")
    form_data = data.get("form_data")

    if not template_key:
        return jsonify({"error": "No se envió template_key"}), 400

    if not form_data:
        return jsonify({"error": "No se enviaron datos del formulario"}), 400

    result = generate_template(template_key, form_data)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
