import customtkinter as ctk
from templates.template_registry import TEMPLATES
from core.generators import generate_template
from ui.dynamic_form import DynamicForm


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("BackOffice HITSS - Generador de Plantillas")
        self.geometry("1100x700")

        self.selected_category = None
        self.selected_template = None

        self._configure_layout()
        self._create_sidebar()
        self._create_main_area()

    # ==============================
    # Layout
    # ==============================

    def _configure_layout(self):
        self.grid_columnconfigure(0, weight=0)  # sidebar
        self.grid_columnconfigure(1, weight=1)  # contenido
        self.grid_rowconfigure(0, weight=1)

    # ==============================
    # Sidebar
    # ==============================

    def _create_sidebar(self):

        self.sidebar = ctk.CTkFrame(self, width=250)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        title = ctk.CTkLabel(
            self.sidebar,
            text="PLANTILLAS",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title.pack(pady=20)

        for category in TEMPLATES.keys():

            category_label = ctk.CTkLabel(
                self.sidebar,
                text=category,
                font=ctk.CTkFont(weight="bold")
            )
            category_label.pack(pady=(15, 5))

            for template_name in TEMPLATES[category].keys():

                btn = ctk.CTkButton(
                    self.sidebar,
                    text=template_name,
                    width=220,
                    command=lambda c=category, t=template_name:
                    self._on_template_selected(c, t)
                )
                btn.pack(pady=3)

    # ==============================
    # Área principal
    # ==============================

    def _create_main_area(self):

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Formulario dinámico
        self.form = DynamicForm(self.main_frame)
        self.form.grid(row=0, column=0, sticky="n", pady=10)

        # Botón generar
        self.generate_button = ctk.CTkButton(
            self.main_frame,
            text="GENERAR PLANTILLA",
            height=40,
            command=self._generate_output
        )
        self.generate_button.grid(row=1, column=0, sticky="ew", pady=10)

        # Output
        self.output_box = ctk.CTkTextbox(self.main_frame)
        self.output_box.grid(row=2, column=0, sticky="nsew")
        self.output_box.configure(font=("Consolas", 12))

    # ==============================
    # Eventos
    # ==============================

    def _on_template_selected(self, category, template_name):

        self.selected_category = category
        self.selected_template = template_name

        self.form.build_form(category, template_name)

    def _generate_output(self):

        if not self.selected_template:
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", "Seleccione una plantilla primero.")
            return

        data = self.form.get_form_data()

        result = generate_template(self.selected_template, data)

        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", result)
