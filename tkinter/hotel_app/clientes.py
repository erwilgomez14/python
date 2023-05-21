import tkinter as tk
from pymongo import MongoClient

class ClientesView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightgrey')

        # Título
        self.label_titulo = tk.Label(self, text="Clientes", font=('Arial', 18))
        self.label_titulo.pack(pady=10)

        # Botón para mostrar el listado
        self.button_listado = tk.Button(self, text="Mostrar Listado", command=self.mostrar_listado)
        self.button_listado.pack(pady=10)

        # Botón para crear un nuevo cliente
        self.button_crear = tk.Button(self, text="Crear Cliente", command=self.mostrar_formulario)
        self.button_crear.pack(side=tk.RIGHT, padx=5, pady=10)
        
        # Etiquetas y campos de entrada
        #self.label_nombre = tk.Label(self, text="Nombre:")
        #self.label_nombre.pack()
        
        #self.entry_nombre = tk.Entry(self)
        #self.entry_nombre.pack()
        
        #self.label_telefono = tk.Label(self, text="Teléfono:")
        #self.label_telefono.pack()
        
        #self.entry_telefono = tk.Entry(self)
        #self.entry_telefono.pack()
        
        # Botón de guardar
        #self.button_guardar = tk.Button(self, text="Guardar", command=self.guardar_cliente)
        #self.button_guardar.pack(pady=10)

        # Configuración del pack del widget principal
        self.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

    def mostrar_formulario(self):
        # Limpiar el formulario anterior si existe
        self.limpiar_formulario()

        # Etiquetas y campos de entrada para el formulario de creación de clientes
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

    def limpiar_formulario(self):
        # Eliminar los elementos del formulario de creación de clientes
        if hasattr(self, 'label_nombre'):
            self.label_nombre.pack_forget()
            self.label_nombre.destroy()
        if hasattr(self, 'entry_nombre'):
            self.entry_nombre.pack_forget()
            self.entry_nombre.destroy()
        if hasattr(self, 'label_telefono'):
            self.label_telefono.pack_forget()
            self.label_telefono.destroy()
        if hasattr(self, 'entry_telefono'):
            self.entry_telefono.pack_forget()
            self.entry_telefono.destroy()
        if hasattr(self, 'button_guardar'):
            self.button_guardar.pack_forget()
            self.button_guardar.destroy()
        
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

    def mostrar_listado(self):
        # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://erwil:2Iu28uUFKF2CfLSu@cluster0.1srnj6u.mongodb.net/?retryWrites=true&w=majority')
        db = client['Hoteleria']
        collection = db['clientes']
        
        # Obtener todos los documentos de la colección
        clientes = collection.find()
        
        # Mostrar el listado de clientes
        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}")
        
        # Cerrar la conexión con MongoDB
        client.close()