import tkinter as tk
from sidebar import Sidebar
from clientes import ClientesView
from suites import SuitesView
from inventario import InventarioView

class HotelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Registro de Hotel")
        self.geometry("800x600")
        
        # Contenedor principal
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sidebar
        self.sidebar = Sidebar(self.main_frame, self.mostrar_vista)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Contenido dinámico
        self.content_frame = tk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Puedes agregar aquí el contenido principal de tu aplicación
        
        # Ejemplo: Etiqueta de bienvenida
        #self.label = tk.Label(self.content_frame, text="Bienvenido", font=('Arial', 18))
        #self.label.pack(padx=20, pady=20)
        
        # Ejemplo: Botón
        #self.button = tk.Button(self.content_frame, text="Click Me", font=('Arial', 14))
        #self.button.pack(padx=20, pady=10)
        
        # Instancias de vistas
        self.clientes_view = ClientesView(self.content_frame)
        self.suites_view = SuitesView(self.content_frame)
        self.inventario_view = InventarioView(self.content_frame)
        
        # Vista actualmente mostrada
        self.vista_actual = None
    
    def mostrar_vista(self, vista):
        if self.vista_actual != vista:
            # Limpiar el contenido actual
            for widget in self.content_frame.winfo_children():
                widget.pack_forget()

            # Mostrar la nueva vista seleccionada
            if vista == "Clientes":
                self.vista_actual = self.clientes_view
            elif vista == "Suites":
                self.vista_actual = self.suites_view
            elif vista == "Inventario":
                self.vista_actual = self.inventario_view

            self.vista_actual.pack(fill=tk.BOTH, expand=True)
        
        # Mantener el sidebar visible
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.content_frame.pack_propagate(0)  # Evitar que el contenido se redimensione
        
if __name__ == "__main__":
    app = HotelApp()
    app.mainloop()