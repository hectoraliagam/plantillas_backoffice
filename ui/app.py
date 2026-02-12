import customtkinter as ctk
from ui.main_window import MainWindow


def run_app():

    # Configuración global
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = MainWindow()
    app.mainloop()
