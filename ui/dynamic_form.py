import customtkinter as ctk
from templates.template_registry import TEMPLATES


class DynamicForm(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.fields = {}
        self.current_template = None

        self.columnconfigure(0, weight=1)

    def build_form(self, category, template_name):

        for widget in self.winfo_children():
            widget.destroy()

        self.fields.clear()
        self.current_template = template_name

        template_data = TEMPLATES[category][template_name]
        fields_config = template_data["fields"]

        for index, field in enumerate(fields_config):

            label = ctk.CTkLabel(self, text=field["label"])
            label.grid(row=index * 2, column=0, sticky="w", padx=10, pady=(10, 2))

            field_type = field.get("type", "entry")

            if field_type == "entry":
                entry = ctk.CTkEntry(self, width=300)
                entry.grid(row=index * 2 + 1, column=0, sticky="ew", padx=10)
                self.fields[field["name"]] = entry

            elif field_type == "textbox":
                textbox = ctk.CTkTextbox(self, height=80)
                textbox.grid(row=index * 2 + 1, column=0, sticky="ew", padx=10)
                self.fields[field["name"]] = textbox

            elif field_type == "combo":
                combo = ctk.CTkComboBox(
                    self,
                    values=field.get("options", []),
                    state="readonly"
                )
                combo.grid(row=index * 2 + 1, column=0, sticky="ew", padx=10)
                self.fields[field["name"]] = combo

    def get_form_data(self):

        data = {}

        for name, widget in self.fields.items():

            if isinstance(widget, ctk.CTkTextbox):
                value = widget.get("1.0", "end").strip()
            else:
                value = widget.get().strip()

            data[name] = value

        return data

    def clear_form(self):

        for widget in self.fields.values():

            if isinstance(widget, ctk.CTkTextbox):
                widget.delete("1.0", "end")
            else:
                widget.delete(0, "end")
