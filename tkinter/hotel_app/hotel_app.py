import tkinter as tk
from inicio_frame import Inicio
from registro_frame import Registro
from consulta_frame import Consulta


class HotelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Registro de Hotel")
        self.geometry("400x300")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self.create_frames()

        self.show_frame('Inicio')

    def create_frames(self):
        for FrameClass in [Inicio, Registro, Consulta]:
            frame_name = FrameClass.__name__
            frame = FrameClass(self.container, self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


if __name__ == "__main__":
    app = HotelApp()
    app.mainloop()
