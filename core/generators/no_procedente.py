# core/generators/no_procedente.py

from templates_registry.constants import get_author

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

REALIZADO POR: {get_author()}
"""

def generar_no_desea_gestion(d):
    return f"""
BACK OFFICE HITSS
CLIENTE NO DESEA FACILIDADES

PROBLEMA REPORTADO: {d['problema']}
CONTACTO: {d['contacto']}
ID DE LLAMADA: {d['id_llamada']}
NUMERO DE TICKET: {d['ticket']}

REALIZADO POR: {get_author()}
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

REALIZADO POR: {get_author()}
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

REALIZADO POR: {get_author()}
"""
