# templates_registry/categories/no_procedente.py

from templates_registry.fields import text_field

NO_PROCEDENTE_TEMPLATES = {

    "SERVICIO_SUSPENDIDO": {
        "category": "NO PROCEDENTE",
        "label": "SERVICIO SUSPENDIDO",
        "fields": [
            text_field("motivo", "Motivo de Suspensión"),
            text_field("fecha", "Fecha de Corte"),
            text_field("contacto", "Contacto"),
            text_field("telefono", "Número Telefónico"),
            text_field("id_llamada", "ID de Llamada"),
            text_field("ticket", "Número de Ticket")
        ]
    },

    "NO_DESEA_GESTION": {
        "category": "NO PROCEDENTE",
        "label": "CLIENTE NO DESEA GESTIÓN",
        "fields": [
            text_field("problema", "Problema Reportado"),
            text_field("contacto", "Contacto"),
            text_field("id_llamada", "ID de Llamada"),
            text_field("ticket", "Número de Ticket")
        ]
    },

    "SOT_EJECUCION": {
        "category": "NO PROCEDENTE",
        "label": "SOT YA EN EJECUCIÓN",
        "fields": [
            text_field("sot", "Número SOT"),
            text_field("fecha", "Fecha"),
            text_field("hora", "Hora"),
            text_field("contacto", "Contacto"),
            text_field("telefono", "Número Telefónico"),
            text_field("id_llamada", "ID de Llamada"),
            text_field("ticket", "Número de Ticket")
        ]
    },

    "FALTA_CONTACTO_CIERRE": {
        "category": "NO PROCEDENTE",
        "label": "FALTA DE CONTACTO (CIERRE)",
        "fields": [
            text_field("telefono", "Número Telefónico"),
            text_field("id_llamada", "ID de Llamada")
        ]
    }

}
