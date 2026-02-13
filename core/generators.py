from templates_registry.template_registry import TEMPLATES, AUTHOR

# ===================== GENERADORES ========================

def generar_sot(d):
    return f"""
VISITA TÉCNICA PROGRAMADA: {d['fecha']} – {d['hora']}
NÚMERO SOT: {d['sot']}

SERVICIO AFECTADO: {d['servicio']}
PROBLEMA REPORTADO POR EL CLIENTE: {d['problema']}
CONTACTO: {d['contacto']}
NÚMERO TELEFÓNICO: {d['telefono']}
DESCARTES REALIZADOS: {d['descartes']}
ID DE LLAMADA: {d['id_llamada']}
NÚMERO DE TICKET: {d['ticket']}

REALIZADO POR: {AUTHOR}
"""

def generar_cierre_conforme(d):
    return f"""
BACK OFFICE HITSS
CLIENTE BRINDA CONFORMIDAD

PROBLEMA REPORTADO: {d['problema']}
SOLUCIÓN APLICADA: {d['solucion']}
DESCARTES: {d['descartes']}
CONTACTO: {d['contacto']}
NÚMERO TELEFÓNICO: {d['telefono']}
ID DE LLAMADA: {d['id_llamada']}
NÚMERO DE TICKET: {d['ticket']}

REALIZADO POR: {AUTHOR}
"""

def generar_no_contesta_1(d):
    return f"""
BACK OFFICE HITSS
CICLO DE LLAMADA NRO: 1
CANTIDAD DE LLAMADAS: 1

NÚMERO TELEFÓNICO: {d['telefono']}
MOTIVO: FALTA DE CONTACTO
SUB-MOTIVO: {d.get('submotivo', '')}
ID DE LLAMADA: {d['id_llamada']}

REALIZADO POR: {AUTHOR}
"""

def generar_no_contesta_2(d):
    return f"""
BACK OFFICE HITSS
CICLO DE LLAMADA NRO: 1
CANTIDAD DE LLAMADAS: 2

NÚMERO TELEFÓNICO: {d['telefono']}
MOTIVO: FALTA DE CONTACTO
SUB-MOTIVO: {d.get('submotivo', '')}
ID DE LLAMADA: {d['id_llamada']}

REALIZADO POR: {AUTHOR}
"""

def generar_devolucion_llamada(d):
    return f"""
BACK OFFICE HITSS
CLIENTE SOLICITA DEVOLUCIÓN DE LLAMADA

MOTIVO: {d['motivo']}
HORARIO SOLICITADO: {d['fecha']} – {d['hora']}
CONTACTO: {d['contacto']}
NÚMERO TELEFÓNICO: {d['telefono']}
ID DE LLAMADA: {d['id_llamada']}

REALIZADO POR: {AUTHOR}
"""

def generar_falta_confirmacion(d):
    return f"""
BackOffice HITSS
PENDIENTE DE CONFIRMACIÓN

GESTIÓN REALIZADA: {d['gestion']}
CONTACTO: {d['contacto']}
NÚMERO TELEFÓNICO: {d['telefono']}
ID DE LLAMADA: {d['id_llamada']}
NÚMERO DE TICKET: {d['ticket']}

REALIZADO POR: {AUTHOR}
"""

def generar_servicio_suspendido(d):
    return f"""
BACK OFFICE HITSS
SERVICIO SUSPENDIDO

MOTIVO DE SUSPENSIÓN: {d['motivo']}
FECHA DE CORTE: {d['fecha']}
SE INFORMA AL CLIENTE: SI
CONTACTO: {d['contacto']}
NÚMERO TELEFÓNICO: {d['telefono']}
ID DE LLAMADA: {d['id_llamada']}
NUMERO DE TICKET: {d['ticket']}

REALIZADO POR: {AUTHOR}
"""

def generar_no_desea_gestion(d):
    return f"""
BACK OFFICE HITSS
CLIENTE NO DESEA FACILIDADES

PROBLEMA REPORTADO: {d['problema']}
CONTACTO: {d['contacto']}
ID DE LLAMADA: {d['id_llamada']}
NUMERO DE TICKET: {d['ticket']}

REALIZADO POR: {AUTHOR}
"""

def generar_sot_ejecucion(d):
    return f"""
BACK OFFICE HITSS
NÚMERO SOT EN EJECUCIÓN: {d['sot']}
FECHA PROGRAMADA: {d['fecha']} – {d['hora']}

SE INFORMA AL CLIENTE: SI
CONTACTO: {d['contacto']}
NÚMERO TELEFÓNICO: {d['telefono']}
ID DE LLAMADA: {d['id_llamada']}
NÚMERO DE TICKET: {d['ticket']}

REALIZADO POR: {AUTHOR}
"""

def generar_falta_contacto_cierre(d):
    return f"""
BackOffice HITSS
CICLO DE LLAMADA NRO: 1
CANTIDAD DE LLAMADAS: 3

NÚMERO TELEFÓNICO: {d['telefono']}
MOTIVO: FALTA DE CONTACTO
SUB-MOTIVO: SE PROCEDE A CIERRE POR INCONTACTABLE
ID DE LLAMADA: {d['id_llamada']}

REALIZADO POR: {AUTHOR}
"""

# ===================== MAPEO CENTRAL ======================

GENERATORS = {
    "SOT_GENERADO": generar_sot,
    "CIERRE_CONFORME": generar_cierre_conforme,
    "NO_CONTESTA_1": generar_no_contesta_1,
    "NO_CONTESTA_2": generar_no_contesta_2,
    "DEVOLUCION_LLAMADA": generar_devolucion_llamada,
    "FALTA_CONFIRMACION": generar_falta_confirmacion,
    "SERVICIO_SUSPENDIDO": generar_servicio_suspendido,
    "NO_DESEA_GESTION": generar_no_desea_gestion,
    "SOT_EJECUCION": generar_sot_ejecucion,
    "FALTA_CONTACTO_CIERRE": generar_falta_contacto_cierre,
}

# =================== FUNCIÓN PRINCIPAL ====================

def generate_template(template_key: str, data: dict) -> str:

    if template_key not in GENERATORS:
        return "❌ Plantilla no válida."

    if template_key not in TEMPLATES:
        return "❌ Plantilla no registrada."

    required_fields = TEMPLATES[template_key]["fields"]

    cleaned_data = {
        k: v.strip() if isinstance(v, str) else v
        for k, v in data.items()
    }

    for field in required_fields:
        field_name = field["name"]
        field_label = field["label"]

        if field_name not in cleaned_data or not cleaned_data[field_name]:
            return f"❌ Falta el campo requerido: {field_label}"

    try:
        return GENERATORS[template_key](cleaned_data).strip()
    except Exception as e:
        return f"❌ Error al generar plantilla: {str(e)}"
