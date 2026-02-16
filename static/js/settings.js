// static/js/settings.js

window.saveSettings = async function () {
  const agent_name = document.getElementById("agent-name").value;
  const agent_code = document.getElementById("agent-code").value;

  const res = await fetch("/settings", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ agent_name, agent_code }),
  });

  const data = await res.json();

  if (data.success) {
    const btn = document.querySelector("button");
    btn.innerText = "Guardado ✓";
    btn.classList.add("bg-green-600");

    setTimeout(() => {
      btn.innerText = "Guardar Cambios";
      btn.classList.remove("bg-green-600");
    }, 2000);
  }
};

window.loadSettings = async function () {
  const res = await fetch("/settings");
  const data = await res.json();

  document.getElementById("agent-name").value = data.agent_name || "";
  document.getElementById("agent-code").value = data.agent_code || "";
};

loadSettings();
