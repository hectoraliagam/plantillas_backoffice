import customtkinter as ctk
from templates.template_registry import TEMPLATES


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):
        super().__init__(parent, width=250)

        self.callback = callback

        ctk.CTkLabel(self, text="PLANTILLAS", font=("Arial", 18, "bold")).pack(pady=20)

        for name in TEMPLATES:
            btn = ctk.CTkButton(
                self,
                text=name,
                command=lambda n=name: self.callback(n)
            )
            btn.pack(fill="x", padx=10, pady=5)
