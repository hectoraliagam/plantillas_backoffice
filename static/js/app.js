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

    let input;

    if (field.type === "combo" && field.options) {
      input = document.createElement("select");
      input.className = "w-full border rounded px-3 py-2";

      field.options.forEach((opt) => {
        const option = document.createElement("option");
        option.value = opt;
        option.innerText = opt;
        input.appendChild(option);
      });
    } else {
      input = document.createElement("input");
      input.type = "text";
      input.className = "w-full border rounded px-3 py-2";
    }

    input.id = field.name;

    wrapper.appendChild(label);
    wrapper.appendChild(input);
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
