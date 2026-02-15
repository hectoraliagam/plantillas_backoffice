// static/js/render/field.factory.js

import { createCopyButton } from "./copy.button.js";

const baseClasses =
  "w-full border border-gray-300 rounded-md px-3 py-2 pr-10 " +
  "focus:outline-none focus:ring-2 focus:ring-slate-800 focus:border-slate-800 transition";

export function createField(field) {
  const wrapper = document.createElement("div");

  const label = document.createElement("label");
  label.innerText = field.label || field.name || "Campo";
  label.className = "block text-sm font-medium mb-1";

  const inputWrapper = document.createElement("div");
  inputWrapper.className = "relative";

  const input = createInput(field);
  input.id = field.name;

  const copyBtn = createCopyButton(input);

  inputWrapper.appendChild(input);
  inputWrapper.appendChild(copyBtn);

  wrapper.appendChild(label);
  wrapper.appendChild(inputWrapper);

  return wrapper;
}

function createInput(field) {
  if (field.type === "combo" && field.options) {
    return createSelect(field.options);
  }

  if (field.type === "date") {
    return createDateInput();
  }

  return createTextInput();
}

function createTextInput() {
  const input = document.createElement("input");
  input.type = "text";
  input.className = baseClasses;
  return input;
}

function createDateInput() {
  const input = document.createElement("input");
  input.type = "date";
  input.className = baseClasses;
  input.value = new Date().toISOString().split("T")[0];
  return input;
}

function createSelect(options) {
  const select = document.createElement("select");
  select.className = baseClasses;

  options.forEach((opt) => {
    const option = document.createElement("option");
    option.value = opt;
    option.innerText = opt;
    select.appendChild(option);
  });

  return select;
}
