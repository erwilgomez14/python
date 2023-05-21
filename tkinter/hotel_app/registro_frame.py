import tkinter as tk

class Registro(tk.Frame):
    def __init__(self, parent, controller):

        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Página de Registro")
        label.pack(pady=10)
        
        volver_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame("Inicio"))
        volver_button.pack()


