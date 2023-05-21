import tkinter as tk
from pymongo import MongoClient

class ClientesView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightgrey')
        
        # Etiquetas y campos de entrada
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.pack()
        
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()
        
        self.label_telefono = tk.Label(self, text="Teléfono:")
        self.label_telefono.pack()
        
        self.entry_telefono = tk.Entry(self)
        self.entry_telefono.pack()
        
        # Botón de guardar
        self.button_guardar = tk.Button(self, text="Guardar", command=self.guardar_cliente)
        self.button_guardar.pack(pady=10)
        
    def guardar_cliente(self):
        # Obtener los valores de los campos de entrada
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        
        # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://erwil:2Iu28uUFKF2CfLSu@cluster0.1srnj6u.mongodb.net/?retryWrites=true&w=majority')
        db = client['Hoteleria']
        collection = db['clientes']
        
        # Crear documento del cliente
        cliente = {
            'nombre': nombre,
            'telefono': telefono
        }
        
        # Insertar el documento en la colección
        collection.insert_one(cliente)
        
        # Cerrar la conexión con MongoDB
        client.close()
        
        # Imprimir mensaje de éxito
        print("Cliente guardado correctamente en MongoDB.")