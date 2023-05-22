import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

class ClientesView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightgrey')

        # Título
        self.label_titulo = tk.Label(self, text="Clientes", font=('Arial', 18))
        self.label_titulo.pack(pady=10)

        # Contenedor para los botones
        self.botones_frame = tk.Frame(self)
        self.botones_frame.pack()

        # Botón para mostrar el listado
        self.button_listado = tk.Button(self.botones_frame, text="Mostrar Listado", command=self.mostrar_listado)
        self.button_listado.pack(side=tk.LEFT, padx=5, pady=10)
        
        # Tabla de clientes
        self.treeview_clientes = ttk.Treeview(self, columns=("Nombre", "Teléfono"))
        self.treeview_clientes.heading("Nombre", text="Nombre")
        self.treeview_clientes.heading("Teléfono", text="Teléfono")
        self.treeview_clientes.pack(pady=10)

        # Botón para crear un nuevo cliente
        self.button_crear = tk.Button(self.botones_frame, text="Crear Cliente", command=self.mostrar_formulario)
        self.button_crear.pack(side=tk.LEFT, padx=5, pady=10)

        # Configuración del pack del widget principal
        self.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

    def mostrar_formulario(self):
        # Ocultar la tabla de clientes
        self.treeview_clientes.pack_forget()

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
        # Limpiar el formulario anterior si existe
        #self.limpiar_formulario()

       

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

    def mostrar_listado(self):
        
        # Ocultar el formulario de creación
        self.limpiar_formulario()
        # Limpiar la tabla
        self.treeview_clientes.delete(*self.treeview_clientes.get_children())

        # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://erwil:2Iu28uUFKF2CfLSu@cluster0.1srnj6u.mongodb.net/?retryWrites=true&w=majority')
        db = client['Hoteleria']
        collection = db['clientes']

        # Obtener todos los documentos de la colección
        clientes = collection.find()

        # Mostrar el listado de clientes en la tabla
        for cliente in clientes:
            nombre = cliente['nombre']
            telefono = cliente['telefono']
            self.treeview_clientes.insert("", "end", values=(nombre, telefono))

        # Cerrar la conexión con MongoDB
        client.close()
        
        self.treeview_clientes.pack(pady=10)