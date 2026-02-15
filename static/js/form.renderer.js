// static/js/form.renderer.js

import { copyField } from "./clipboard.js";
import { state } from "./state.js";

export function renderForm() {
  const form = document.getElementById("dynamic-form");
  form.innerHTML = "";

  if (!state.templateFields.length) {
    form.innerHTML =
      "<p class='text-gray-500'>Esta plantilla no tiene campos definidos.</p>";
    return;
  }

  state.templateFields.forEach((field) => {
    const wrapper = document.createElement("div");

    const label = document.createElement("label");
    label.innerText = field.label || field.name || "Campo";
    label.className = "block text-sm font-medium mb-1";

    const inputWrapper = document.createElement("div");
    inputWrapper.className = "relative";

    let input;

    if (field.type === "combo" && field.options) {
      input = document.createElement("select");
      input.className =
        "w-full border border-gray-300 rounded-md px-3 py-2 pr-10 focus:outline-none focus:ring-2 focus:ring-slate-800 focus:border-slate-800 transition";

      field.options.forEach((opt) => {
        const option = document.createElement("option");
        option.value = opt;
        option.innerText = opt;
        input.appendChild(option);
      });
    } else {
      input = document.createElement("input");
      input.type = "text";
      input.className =
        "w-full border border-gray-300 rounded-md px-3 py-2 pr-10 focus:outline-none focus:ring-2 focus:ring-slate-800 focus:border-slate-800 transition";
    }

    input.id = field.name;

    const copyBtn = document.createElement("button");
    copyBtn.type = "button";
    copyBtn.className =
      "absolute right-0 top-0 h-full w-10 flex items-center justify-center text-gray-400 hover:text-slate-900 transition";

    copyBtn.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg"
           class="w-5 h-5"
           fill="none"
           viewBox="0 0 24 24"
           stroke="currentColor"
           stroke-width="1.5">
          <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>
          <path d="M5 15H4a2 2 0 0 1-2-2V4
                   a2 2 0 0 1 2-2h9
                   a2 2 0 0 1 2 2v1"/>
      </svg>
    `;

    copyBtn.addEventListener("click", () => copyField(input));

    copyBtn.style.opacity = "0.3";

    input.addEventListener("input", () => {
      copyBtn.style.opacity = input.value ? "1" : "0.3";
    });

    inputWrapper.appendChild(input);
    inputWrapper.appendChild(copyBtn);

    wrapper.appendChild(label);
    wrapper.appendChild(inputWrapper);

    form.appendChild(wrapper);
  });
}
