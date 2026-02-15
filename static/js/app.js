// static/js/app.js

let selectedTemplate = null;
let templateFields = [];

function selectTemplate(templateKey) {
  selectedTemplate = templateKey;
  templateFields = [];

  for (const categoria in TEMPLATES) {
    if (TEMPLATES[categoria][templateKey]) {
      templateFields = TEMPLATES[categoria][templateKey].fields || [];
      document.getElementById("template-title").innerText =
        TEMPLATES[categoria][templateKey].label;
      break;
    }
  }

  renderForm();
}

function renderForm() {
  const form = document.getElementById("dynamic-form");
  form.innerHTML = "";

  if (!templateFields.length) {
    form.innerHTML =
      "<p class='text-gray-500'>Esta plantilla no tiene campos definidos.</p>";
    return;
  }

  templateFields.forEach((field) => {
    const wrapper = document.createElement("div");

    const label = document.createElement("label");
    label.innerText = field.label || field.name || "Campo";
    label.className = "block text-sm font-medium mb-1";

    const inputWrapper = document.createElement("div");
    inputWrapper.className = "relative";

    let input;

    if (field.type === "combo" && field.options) {
      input = document.createElement("select");
      input.className = "w-full border rounded px-3 py-2 pr-10";

      field.options.forEach((opt) => {
        const option = document.createElement("option");
        option.value = opt;
        option.innerText = opt;
        input.appendChild(option);
      });
    } else {
      input = document.createElement("input");
      input.type = "text";
      input.className = "w-full border rounded px-3 py-2 pr-10";
    }

    input.id = field.name;

    const copyBtn = document.createElement("button");
    copyBtn.type = "button";
    copyBtn.className =
      "absolute right-0 top-0 h-full w-10 border-l bg-gray-50 hover:bg-gray-100 transition flex items-center justify-center";
    copyBtn.onclick = () => copyField(field.name);

    copyBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg"
             class="w-4 h-4 text-gray-600"
             fill="none"
             viewBox="0 0 24 24"
             stroke="currentColor"
             stroke-width="2">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>
            <path d="M5 15H4a2 2 0 0 1-2-2V4
                     a2 2 0 0 1 2-2h9
                     a2 2 0 0 1 2 2v1"/>
        </svg>
    `;

    inputWrapper.appendChild(input);
    inputWrapper.appendChild(copyBtn);

    wrapper.appendChild(label);
    wrapper.appendChild(inputWrapper);

    form.appendChild(wrapper);
  });
}

function generateTemplate() {
  if (!selectedTemplate) {
    alert("Selecciona una plantilla primero.");
    return;
  }

  const formData = {};

  templateFields.forEach((field) => {
    formData[field.name] = document.getElementById(field.name)?.value || "";
  });

  fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      template_key: selectedTemplate,
      form_data: formData,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.result) {
        document.getElementById("result-box").value = data.result;
      } else if (data.error) {
        alert(data.error);
      } else {
        alert("Error generando plantilla.");
      }
    });
}

function copyResult() {
  const textarea = document.getElementById("result-box");
  textarea.select();
  document.execCommand("copy");
}

function copyField(fieldId) {
  const input = document.getElementById(fieldId);
  if (!input) return;

  navigator.clipboard.writeText(input.value);

  input.classList.add("ring-2", "ring-green-500");

  setTimeout(() => {
    input.classList.remove("ring-2", "ring-green-500");
  }, 500);
}
