import tkinter 

def barra_menu(root):
    barra_menu = tkinter.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    memu_inicio = tkinter.Menu(barra_menu , tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu= memu_inicio)

    memu_inicio.add_command(label='Crear Registro en BD')
    memu_inicio.add_command(label='Eliminar Registro en BD')
    memu_inicio.add_command(label='Salir', command= root.destroy)
class Frame(tkinter.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 480, height=320)
        self.root = root
        self.pack()
        self.config( bg='red')