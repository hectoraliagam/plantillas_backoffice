const rawTemplates = document.getElementById("templates-data");

export const TEMPLATES = rawTemplates
  ? JSON.parse(rawTemplates.textContent)
  : {};
