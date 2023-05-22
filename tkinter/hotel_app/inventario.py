import tkinter as tk
from pymongo import MongoClient

class InventarioView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightgray')
        
        # Etiquetas y campos de entrada
        self.label_nombre = tk.Label(self, text="nombre :")
        self.label_nombre.pack()
        
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()
        
        self.label_precio = tk.Label(self, text="precio :")
        self.label_precio.pack()
        
        self.entry_precio = tk.Entry(self)
        self.entry_precio.pack()

        self.label_numero = tk.Label(self, text="id :")
        self.label_numero.pack()

        self.entry_numero = tk.Entry(self)
        self.entry_numero.pack()
        
        # Botón de guardar
        self.button_guardar = tk.Button(self, text="Guardar", command=self.guardar_inventario)
        self.button_guardar.pack(pady=10)

        # Configuración del pack del widget principal
        self.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
    def guardar_inventario(self):
        # Aquí puedes agregar la lógica para guardar los datos del inventario en tu base de datos
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        id = self.entry_numero.get()
        
        # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://erwil:2Iu28uUFKF2CfLSu@cluster0.1srnj6u.mongodb.net/?retryWrites=true&w=majority')
        db = client['Hoteleria']
        collection = db['inventario']
        
        # Crear documento del cliente
        cliente = {
            'nombre': nombre,
            'precio': precio,
            'id': id
        }
        
        # Insertar el documento en la colección
        collection.insert_one(cliente)
        
        # Cerrar la conexión con MongoDB
        client.close()
        
        # Imprimir mensaje de éxito
        print("Suite guardada correctamente en MongoDB.")
        # Obtener los valores de los campos de entrada
        
        
        # Imprimir los valores
        print(f"nombre: {nombre}")
        print(f"precio: {precio}")
        print(f"id: {id}")
