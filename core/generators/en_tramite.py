# core/generators/en_tramite.py

from templates_registry.constants import AUTHOR

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
