// static/js/render/form.renderer.js

import { state } from "../state.js";
import { createField } from "./field.factory.js";

export function renderForm() {
  const form = document.getElementById("dynamic-form");
  form.innerHTML = "";

  if (!state.templateFields.length) {
    form.innerHTML =
      "<p class='text-gray-500'>Esta plantilla no tiene campos definidos.</p>";
    return;
  }

  state.templateFields.forEach((field) => {
    const fieldElement = createField(field);
    form.appendChild(fieldElement);
  });
}
