// static/js/clipboard.js

export function copyField(input) {
  if (!input) return;

  navigator.clipboard.writeText(input.value);

  input.classList.add("ring-2", "ring-slate-800");

  setTimeout(() => {
    input.classList.remove("ring-2", "ring-slate-800");
  }, 500);
}

export function copyTextarea(textarea) {
  navigator.clipboard.writeText(textarea.value);
}
