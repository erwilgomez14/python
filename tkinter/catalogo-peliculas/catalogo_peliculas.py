import tkinter 
from client.gui_app import Frame, barra_menu
def main():
    root = tkinter.Tk()
    root.title('The Annu')
    root.iconbitmap('img/macuahuitl.ico')
    root.resizable(0,0)
    barra_menu(root)
    app = Frame(root = root)
    


    app.mainloop()

if __name__ == '__main__':
    main()