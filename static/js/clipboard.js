// static/js/clipboard.js

function formatDateIfNeeded(input) {
  if (input.type !== "date") return input.value;

  const [year, month, day] = input.value.split("-");
  return `${day}/${month}/${year}`;
}

export function copyField(input) {
  if (!input) return;

  const value = formatDateIfNeeded(input);

  navigator.clipboard.writeText(value);

  input.classList.add("ring-2", "ring-slate-800");

  setTimeout(() => {
    input.classList.remove("ring-2", "ring-slate-800");
  }, 500);
}

export function copyTextarea(textarea) {
  navigator.clipboard.writeText(textarea.value);
}
