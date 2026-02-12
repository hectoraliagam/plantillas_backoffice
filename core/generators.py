from core.constants import AUTHOR_SIGNATURE


# ===== PROCEDENTE =====

def generar_sot_generado(data):
    return f"""VISITA TÉCNICA PROGRAMADA: {data['fecha']} – {data['hora']}
NÚMERO SOT: {data['sot']}

SERVICIO AFECTADO: {data['servicio']}
PROBLEMA REPORTADO POR EL CLIENTE: {data['problema']}
CONTACTO: {data['contacto']}
NÚMERO TELEFÓNICO: {data['telefono']}
DESCARTES REALIZADOS: {data['descartes']}
ID DE LLAMADA: {data['id_llamada']}
NÚMERO DE TICKET: {data['ticket']}

{AUTHOR_SIGNATURE}
"""

def generar_cierre_cliente_conforme(data):
    return f"""BACK OFFICE HITSS
CLIENTE BRINDA CONFORMIDAD

PROBLEMA REPORTADO: {data['problema']}
SOLUCIÓN APLICADA: {data['solucion']}
DESCARTES: {data['descartes']}
CONTACTO: {data['contacto']}
NÚMERO TELEFÓNICO: {data['telefono']}
ID DE LLAMADA: {data['id_llamada']}
NÚMERO DE TICKET: {data['ticket']}

{AUTHOR_SIGNATURE}
"""


# ===== EN TRÁMITE =====

def generar_no_contesta_1ra(data):
    return f"""BACK OFFICE HITSS
CICLO DE LLAMADA NRO: 1
CANTIDAD DE LLAMADAS: 1

NÚMERO TELEFÓNICO: {data['telefono']}
MOTIVO: FALTA DE CONTACTO
SUB-MOTIVO: {data['submotivo']}
ID DE LLAMADA: {data['id_llamada']}

{AUTHOR_SIGNATURE}
"""

def generar_no_contesta_2da(data):
    return f"""BACK OFFICE HITSS
CICLO DE LLAMADA NRO: 1
CANTIDAD DE LLAMADAS: 2

NÚMERO TELEFÓNICO: {data['telefono']}
MOTIVO: FALTA DE CONTACTO
SUB-MOTIVO: {data['submotivo']}
ID DE LLAMADA: {data['id_llamada']}

{AUTHOR_SIGNATURE}
"""

def generar_devolucion_llamada(data):
    return f"""BACK OFFICE HITSS
CLIENTE SOLICITA DEVOLUCIÓN DE LLAMADA

MOTIVO: {data['motivo']}
HORARIO SOLICITADO: {data['fecha']} – {data['hora']}
CONTACTO: {data['contacto']}
NÚMERO TELEFÓNICO: {data['telefono']}
ID DE LLAMADA: {data['id_llamada']}

{AUTHOR_SIGNATURE}
"""

def generar_falta_confirmacion(data):
    return f"""BackOffice HITSS
PENDIENTE DE CONFIRMACIÓN

GESTIÓN REALIZADA: {data['gestion']}
CONTACTO: {data['contacto']}
NÚMERO TELEFÓNICO: {data['telefono']}
ID DE LLAMADA: {data['id_llamada']}
NÚMERO DE TICKET: {data['ticket']}

{AUTHOR_SIGNATURE}
"""


# ===== NO PROCEDENTE =====

def generar_servicio_suspendido(data):
    return f"""BACK OFFICE HITSS
SERVICIO SUSPENDIDO

MOTIVO DE SUSPENSIÓN: {data['motivo']}
FECHA DE CORTE: {data['fecha_corte']}
SE INFORMA AL CLIENTE: SI
CONTACTO: {data['contacto']}
NÚMERO TELEFÓNICO: {data['telefono']}
ID DE LLAMADA: {data['id_llamada']}
NÚMERO DE TICKET: {data['ticket']}

{AUTHOR_SIGNATURE}
"""

def generar_cliente_no_desea(data):
    return f"""BACK OFFICE HITSS
CLIENTE NO DESEA FACILIDADES

PROBLEMA REPORTADO: {data['problema']}
CONTACTO: {data['contacto']}
ID DE LLAMADA: {data['id_llamada']}
NÚMERO DE TICKET: {data['ticket']}

{AUTHOR_SIGNATURE}
"""

def generar_sot_en_ejecucion(data):
    return f"""BACK OFFICE HITSS
NÚMERO SOT EN EJECUCIÓN: {data['sot']}
FECHA PROGRAMADA: {data['fecha']} – {data['hora']}

SE INFORMA AL CLIENTE: SI
CONTACTO: {data['contacto']}
NÚMERO TELEFÓNICO: {data['telefono']}
ID DE LLAMADA: {data['id_llamada']}
NÚMERO DE TICKET: {data['ticket']}

{AUTHOR_SIGNATURE}
"""

def generar_falta_contacto_cierre(data):
    return f"""BackOffice HITSS
CICLO DE LLAMADA NRO: 1
CANTIDAD DE LLAMADAS: 3

NÚMERO TELEFÓNICO: {data['telefono']}
MOTIVO: FALTA DE CONTACTO
SUB-MOTIVO: SE PROCEDE A CIERRE POR INCONTACTABLE
ID DE LLAMADA: {data['id_llamada']}

{AUTHOR_SIGNATURE}
"""


# ===== DISPATCHER PRINCIPAL =====

def generate_template(template_name, data):

    generators = {
        "SOT GENERADO": generar_sot_generado,
        "CIERRE CLIENTE CONFORME": generar_cierre_cliente_conforme,
        "CLIENTE NO CONTESTA 1RA LLAMADA": generar_no_contesta_1ra,
        "CLIENTE NO CONTESTA 2DA LLAMADA": generar_no_contesta_2da,
        "CLIENTE SOLICITA DEVOLUCIÓN DE LLAMADA": generar_devolucion_llamada,
        "FALTA CONFIRMACIÓN DEL CLIENTE": generar_falta_confirmacion,
        "SERVICIO SUSPENDIDO": generar_servicio_suspendido,
        "CLIENTE NO DESEA GESTIÓN": generar_cliente_no_desea,
        "SOT YA EN EJECUCIÓN": generar_sot_en_ejecucion,
        "FALTA DE CONTACTO (CIERRE)": generar_falta_contacto_cierre,
    }

    generator = generators.get(template_name)

    if not generator:
        return "Plantilla no encontrada."

    return generator(data)
