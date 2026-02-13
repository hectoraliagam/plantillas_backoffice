AUTHOR = "HECTOR GABRIEL ALIAGA MEDINA / E759929"

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

TEMPLATES = {

    # ===================== PROCEDENTE =====================

    "SOT_GENERADO": {
        "category": "PROCEDENTE",
        "label": "SOT GENERADO",
        "fields": [
            text_field("fecha", "Fecha"),
            text_field("hora", "Hora"),
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
    },

    # ===================== EN TRÁMITE =====================

    "NO_CONTESTA_1": {
        "category": "EN TRÁMITE",
        "label": "CLIENTE NO CONTESTA 1RA LLAMADA",
        "fields": [
            text_field("telefono", "Número Telefónico"),
            combo_field(
                "submotivo",
                "Submotivo",
                ["Buzón de voz", "No contesta", "Número no existe", "Apagado", "Corta llamada"]
            ),
            text_field("id_llamada", "ID de Llamada")
        ]
    },

    "NO_CONTESTA_2": {
        "category": "EN TRÁMITE",
        "label": "CLIENTE NO CONTESTA 2DA LLAMADA",
        "fields": [
            text_field("telefono", "Número Telefónico"),
            combo_field(
                "submotivo",
                "Submotivo",
                ["Buzón de voz", "No contesta", "Número no existe", "Apagado", "Corta llamada"]
            ),
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
    },

    # ==================== NO PROCEDENTE ===================

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
