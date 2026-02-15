// static/js/template.service.js

export function findTemplate(templateKey) {
  for (const categoria in TEMPLATES) {
    if (TEMPLATES[categoria][templateKey]) {
      return TEMPLATES[categoria][templateKey];
    }
  }
  return null;
}
