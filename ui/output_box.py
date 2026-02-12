import customtkinter as ctk


class OutputBox(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Resultado", font=("Arial", 16, "bold")).pack(pady=10)

        self.textbox = ctk.CTkTextbox(self, wrap="word")
        self.textbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.copy_btn = ctk.CTkButton(
            self,
            text="Copiar al portapapeles",
            command=self.copy_text
        )
        self.copy_btn.pack(pady=10)

    def set_text(self, text):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)

    def copy_text(self):
        text = self.textbox.get("1.0", "end")
        self.clipboard_clear()
        self.clipboard_append(text)
