import tkinter as tk

class Inicio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Página de Inicio")
        label.pack(pady=10)
        
        registro_button = tk.Button(self, text="Registro", command=lambda: controller.show_frame("Registro"))
        registro_button.pack()
        
        consulta_button = tk.Button(self, text="Consulta", command=lambda: controller.show_frame("Consulta"))
        consulta_button.pack()