# templates_registry/categories/procedente.py

from templates_registry.fields import text_field, combo_field, date_field, time_range_field

PROCEDENTE_TEMPLATES = {

    "SOT_GENERADO": {
        "category": "PROCEDENTE",
        "label": "SOT GENERADO",
        "fields": [
            date_field("fecha", "Fecha"),
            time_range_field("hora", "Hora"),
            text_field("sot", "Número SOT"),
            combo_field("servicio", "Servicio", ["TELEFONÍA", "INTERNET", "CABLE"]),
            text_field("problema", "Problema Reportado"),
            text_field("contacto", "Nombre de Contacto"),
            text_field("telefono", "Número Telefónico"),
            text_field("descartes", "Descartes Realizados"),
            text_field("id_llamada", "ID de Llamada"),
            text_field("ticket", "Número de Ticket")
        ]
    },

    "CIERRE_CONFORME": {
        "category": "PROCEDENTE",
        "label": "CIERRE CLIENTE CONFORME",
        "fields": [
            text_field("problema", "Problema Reportado"),
            text_field("solucion", "Solución Aplicada"),
            text_field("descartes", "Descartes"),
            text_field("contacto", "Contacto"),
            text_field("telefono", "Número Telefónico"),
            text_field("id_llamada", "ID de Llamada"),
            text_field("ticket", "Número de Ticket")
        ]
    }

}
