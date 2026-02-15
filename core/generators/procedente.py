# core/generators/procedente.py

from templates_registry.constants import AUTHOR

def generar_sot(d):
    return f"""
VISITA TÉCNICA PROGRAMADA: {d['fecha']} | {d['hora']}
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
