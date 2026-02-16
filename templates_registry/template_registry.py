# templates_registry/template_registry.py

from templates_registry.categories.procedente import PROCEDENTE_TEMPLATES
from templates_registry.categories.en_tramite import EN_TRAMITE_TEMPLATES
from templates_registry.categories.no_procedente import NO_PROCEDENTE_TEMPLATES

TEMPLATES = {
    **PROCEDENTE_TEMPLATES,
    **EN_TRAMITE_TEMPLATES,
    **NO_PROCEDENTE_TEMPLATES,
}
