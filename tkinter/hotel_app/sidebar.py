import tkinter as tk
import sys
from clientes import ClientesView
from suites import SuitesView

class Sidebar(tk.Frame):
    def __init__(self, parent, mostrar_vista):
        super().__init__(parent)
        self.mostrar_vista = mostrar_vista
        self.configure(bg='lightblue')
        
        
        # Frame del logo y título
        self.frame_logo = tk.Frame(self, bg='white', height=100)
        self.frame_logo.pack(fill=tk.X)
        
        # Logo
        self.logo_label = tk.Label(self.frame_logo, text="Logo", font=('Arial', 20), bg='white')
        self.logo_label.pack(pady=10)
        
        # Título
        self.title_label = tk.Label(self.frame_logo, text="Hotel", font=('Arial', 18), bg='white')
        self.title_label.pack()
        
        # Frame de secciones
        self.frame_secciones = tk.Frame(self, bg='lightblue')
        self.frame_secciones.pack(fill=tk.X, padx=10, pady=20)
        
        # Botones de secciones
        self.btn_seccion1 = tk.Button(self.frame_secciones, text="Clientes", font=('Arial', 12), width=15, command=lambda: self.mostrar_vista("Clientes"))
        self.btn_seccion1.pack(pady=5)
        
        self.btn_seccion2 = tk.Button(self.frame_secciones, text="Suites", font=('Arial', 12), width=15, command=lambda: self.mostrar_vista("Suites"))
        self.btn_seccion2.pack(pady=5)
        
        self.btn_seccion3 = tk.Button(self.frame_secciones, text="inventario", font=('Arial', 12), width=15)
        self.btn_seccion3.pack(pady=5)
        
         # Botón de salida
        self.btn_exit = tk.Button(self, text="Salir", font=('Arial', 12), command=self.exit_program)
        self.btn_exit.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        
    def exit_program(self):
        sys.exit(0)
    
    def mostrar_clientes_view(self):
        #self.pack_forget()  # Ocultar el Sidebar actual
        #self.destroy()  # Destruir el sidebar actual
        clientes_view = ClientesView(self.master)  # Crear la vista de clientes
        clientes_view.pack(fill=tk.BOTH, expand=True)
        
    def mostrar_suites_view(self):
        # Ocultar el Sidebar actual
        #self.pack_forget()
        
        # Crear la vista de suites
        suites_view = SuitesView(self.master)
        suites_view.pack(fill=tk.BOTH, expand=True)
        #self.parent.mostrar_vista("Suites")  # Llamar a la función mostrar_vista del padre
