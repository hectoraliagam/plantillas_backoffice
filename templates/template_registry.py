TEMPLATES = {

    "PROCEDENTE": {

        "SOT GENERADO": {
            "fields": [
                {"name": "fecha", "label": "Fecha"},
                {"name": "hora", "label": "Hora"},
                {
                    "name": "servicio",
                    "label": "Servicio Afectado",
                    "type": "combo",
                    "options": ["TELEFONÍA", "INTERNET", "CABLE"]
                },
                {"name": "sot", "label": "Número SOT"},
                {"name": "problema", "label": "Problema Reportado"},
                {"name": "contacto", "label": "Contacto"},
                {"name": "telefono", "label": "Número Telefónico"},
                {"name": "descartes", "label": "Descartes Realizados"},
                {"name": "id_llamada", "label": "ID de Llamada"},
                {"name": "ticket", "label": "Número de Ticket"},
            ]
        },

        "CIERRE CLIENTE CONFORME": {
            "fields": [
                {"name": "problema", "label": "Problema Reportado"},
                {"name": "solucion", "label": "Solución Aplicada"},
                {"name": "descartes", "label": "Descartes"},
                {"name": "contacto", "label": "Contacto"},
                {"name": "telefono", "label": "Número Telefónico"},
                {"name": "id_llamada", "label": "ID de Llamada"},
                {"name": "ticket", "label": "Número de Ticket"},
            ]
        }
    },

    "EN TRÁMITE": {

        "CLIENTE NO CONTESTA 1RA LLAMADA": {
            "fields": [
                {"name": "telefono", "label": "Número Telefónico"},
                {
                    "name": "submotivo",
                    "label": "Sub-motivo",
                    "type": "combo",
                    "options": [
                        "Buzón de voz",
                        "No contesta",
                        "Número no existe",
                        "Apagado",
                        "Corta llamada"
                    ]
                },
                {"name": "id_llamada", "label": "ID de Llamada"},
            ]
        },

        "CLIENTE NO CONTESTA 2DA LLAMADA": {
            "fields": [
                {"name": "telefono", "label": "Número Telefónico"},
                {
                    "name": "submotivo",
                    "label": "Sub-motivo",
                    "type": "combo",
                    "options": [
                        "Buzón de voz",
                        "No contesta",
                        "Número no existe",
                        "Apagado",
                        "Corta llamada"
                    ]
                },
                {"name": "id_llamada", "label": "ID de Llamada"},
            ]
        },

        "CLIENTE SOLICITA DEVOLUCIÓN DE LLAMADA": {
            "fields": [
                {"name": "motivo", "label": "Motivo"},
                {"name": "fecha", "label": "Fecha"},
                {"name": "hora", "label": "Hora"},
                {"name": "contacto", "label": "Contacto"},
                {"name": "telefono", "label": "Número Telefónico"},
                {"name": "id_llamada", "label": "ID de Llamada"},
            ]
        },

        "FALTA CONFIRMACIÓN DEL CLIENTE": {
            "fields": [
                {"name": "gestion", "label": "Gestión Realizada"},
                {"name": "contacto", "label": "Contacto"},
                {"name": "telefono", "label": "Número Telefónico"},
                {"name": "id_llamada", "label": "ID de Llamada"},
                {"name": "ticket", "label": "Número de Ticket"},
            ]
        }
    },

    "NO PROCEDENTE": {

        "SERVICIO SUSPENDIDO": {
            "fields": [
                {"name": "motivo", "label": "Motivo de Suspensión"},
                {"name": "fecha_corte", "label": "Fecha de Corte"},
                {"name": "contacto", "label": "Contacto"},
                {"name": "telefono", "label": "Número Telefónico"},
                {"name": "id_llamada", "label": "ID de Llamada"},
                {"name": "ticket", "label": "Número de Ticket"},
            ]
        },

        "CLIENTE NO DESEA GESTIÓN": {
            "fields": [
                {"name": "problema", "label": "Problema Reportado"},
                {"name": "contacto", "label": "Contacto"},
                {"name": "id_llamada", "label": "ID de Llamada"},
                {"name": "ticket", "label": "Número de Ticket"},
            ]
        },

        "SOT YA EN EJECUCIÓN": {
            "fields": [
                {"name": "sot", "label": "Número SOT en Ejecución"},
                {"name": "fecha", "label": "Fecha"},
                {"name": "hora", "label": "Hora"},
                {"name": "contacto", "label": "Contacto"},
                {"name": "telefono", "label": "Número Telefónico"},
                {"name": "id_llamada", "label": "ID de Llamada"},
                {"name": "ticket", "label": "Número de Ticket"},
            ]
        },

        "FALTA DE CONTACTO (CIERRE)": {
            "fields": [
                {"name": "telefono", "label": "Número Telefónico"},
                {"name": "id_llamada", "label": "ID de Llamada"},
            ]
        }
    }
}
