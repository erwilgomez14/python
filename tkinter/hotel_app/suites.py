import tkinter as tk
from pymongo import MongoClient

class SuitesView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightblue')
        
        # Etiquetas y campos de entrada
        self.label_numero = tk.Label(self, text="Número de suite:")
        self.label_numero.pack()
        
        self.entry_numero = tk.Entry(self)
        self.entry_numero.pack()
        
        self.label_tipo = tk.Label(self, text="Tipo de suite:")
        self.label_tipo.pack()
        
        self.entry_tipo = tk.Entry(self)
        self.entry_tipo.pack()
        
        # Botón de guardar
        self.button_guardar = tk.Button(self, text="Guardar", command=self.guardar_suite)
        self.button_guardar.pack(pady=10)
        
    def guardar_suite(self):
        # Aquí puedes agregar la lógica para guardar los datos de la suite en tu base de datos
        numero = self.entry_numero.get()
        tipo = self.entry_tipo.get()
         # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://erwil:2Iu28uUFKF2CfLSu@cluster0.1srnj6u.mongodb.net/?retryWrites=true&w=majority')
        db = client['Hoteleria']
        collection = db['suites']
        
        # Crear documento del cliente
        cliente = {
            'numero_suite': numero,
            'tipo_suite': tipo
        }
        
        # Insertar el documento en la colección
        collection.insert_one(cliente)
        
        # Cerrar la conexión con MongoDB
        client.close()
        
        # Imprimir mensaje de éxito
        print("Suite guardada correctamente en MongoDB.")
        # Obtener los valores de los campos de entrada
        
        
        # Imprimir los valores
        print(f"Número de suite: {numero}")
        print(f"Tipo de suite: {tipo}")