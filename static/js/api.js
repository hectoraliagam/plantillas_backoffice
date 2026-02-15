// static/js/api.js

export async function generateTemplateAPI(templateKey, formData) {
  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      template_key: templateKey,
      form_data: formData,
    }),
  });

  return res.json();
}
