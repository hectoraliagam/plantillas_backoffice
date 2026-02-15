// static/js/render/copy.button.js

import { copyField } from "../clipboard.js";

export function createCopyButton(input) {
  const btn = document.createElement("button");
  btn.type = "button";

  btn.className =
    "absolute right-0 top-0 h-full w-10 flex items-center justify-center " +
    "text-gray-400 hover:text-slate-900 transition";

  btn.innerHTML = `
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

  btn.style.opacity = "0.3";

  input.addEventListener("input", () => {
    btn.style.opacity = input.value ? "1" : "0.3";
  });

  btn.addEventListener("click", () => copyField(input));

  return btn;
}
