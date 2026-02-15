// static/js/state.js

export const state = {
  selectedTemplate: null,
  templateFields: [],
};

export function setTemplate(key, fields) {
  state.selectedTemplate = key;
  state.templateFields = fields || [];
}
