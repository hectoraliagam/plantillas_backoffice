# core/registry.py

from core.generators.procedente import (
    generar_sot,
    generar_cierre_conforme
)

from core.generators.en_tramite import (
    generar_no_contesta_1,
    generar_no_contesta_2,
    generar_devolucion_llamada,
    generar_falta_confirmacion
)

from core.generators.no_procedente import (
    generar_servicio_suspendido,
    generar_no_desea_gestion,
    generar_sot_ejecucion,
    generar_falta_contacto_cierre
)

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
