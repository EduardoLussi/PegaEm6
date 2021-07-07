from tkinter import *


class MenuIniciar(Frame):
    def __init__(self, master, parent_root):
        Frame.__init__(self, master)

        self.parent_root = parent_root

        self.master.title("Menu Iniciar")
        self.master.geometry(f"{self.parent_root.winfo_screenwidth()}x{self.parent_root.winfo_screenheight()}")

        self.button = Button(self, text='Iniciar Jogo', command=lambda: self.handle_event())
        self.button.pack()

        self.pack()

    def handle_event(self):
        self.master.destroy()
        self.parent_root.deiconify()
