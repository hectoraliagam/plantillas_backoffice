// static/js/app.js

import { setTemplate, state } from "./state.js";
import { findTemplate } from "./template.service.js";
import { renderForm } from "./form.renderer.js";
import { generateTemplateAPI } from "./api.js";
import { copyTextarea } from "./clipboard.js";

window.selectTemplate = function (templateKey) {
  const template = findTemplate(templateKey);
  if (!template) return;

  setTemplate(templateKey, template.fields);
  document.getElementById("template-title").innerText = template.label;

  renderForm();
};

window.generateTemplate = async function () {
  if (!state.selectedTemplate) {
    alert("Selecciona una plantilla primero.");
    return;
  }

  const formData = {};

  state.templateFields.forEach((field) => {
    formData[field.name] = document.getElementById(field.name)?.value || "";
  });

  const data = await generateTemplateAPI(state.selectedTemplate, formData);

  if (data.result) {
    document.getElementById("result-box").value = data.result;
  } else {
    alert(data.error || "Error generando plantilla.");
  }
};

window.copyResult = function () {
  const textarea = document.getElementById("result-box");
  copyTextarea(textarea);
};
