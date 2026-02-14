# templates_registry/categories/en_tramite.py

from templates_registry.fields import text_field, combo_field

SUBMOTIVOS = [
    "Buzón de voz",
    "No contesta",
    "Número no existe",
    "Apagado",
    "Corta llamada"
]

EN_TRAMITE_TEMPLATES = {

    "NO_CONTESTA_1": {
        "category": "EN TRÁMITE",
        "label": "CLIENTE NO CONTESTA 1RA LLAMADA",
        "fields": [
            text_field("telefono", "Número Telefónico"),
            combo_field("submotivo", "Submotivo", SUBMOTIVOS),
            text_field("id_llamada", "ID de Llamada")
        ]
    },

    "NO_CONTESTA_2": {
        "category": "EN TRÁMITE",
        "label": "CLIENTE NO CONTESTA 2DA LLAMADA",
        "fields": [
            text_field("telefono", "Número Telefónico"),
            combo_field("submotivo", "Submotivo", SUBMOTIVOS),
            text_field("id_llamada", "ID de Llamada")
        ]
    },

    "DEVOLUCION_LLAMADA": {
        "category": "EN TRÁMITE",
        "label": "CLIENTE SOLICITA DEVOLUCIÓN DE LLAMADA",
        "fields": [
            text_field("motivo", "Motivo"),
            text_field("fecha", "Fecha"),
            text_field("hora", "Hora"),
            text_field("contacto", "Contacto"),
            text_field("telefono", "Número Telefónico"),
            text_field("id_llamada", "ID de Llamada")
        ]
    },

    "FALTA_CONFIRMACION": {
        "category": "EN TRÁMITE",
        "label": "FALTA CONFIRMACIÓN DEL CLIENTE",
        "fields": [
            text_field("gestion", "Gestión Realizada"),
            text_field("contacto", "Contacto"),
            text_field("telefono", "Número Telefónico"),
            text_field("id_llamada", "ID de Llamada"),
            text_field("ticket", "Número de Ticket")
        ]
    }

}
