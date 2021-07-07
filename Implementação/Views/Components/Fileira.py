from tkinter import *
from os import path


class Fileira(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master)
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.cartas = [PhotoImage(file=f"{pathName}/img/cartas/9.png")] * 5
        self.atualizarCartas()

    def atualizarCartas(self):
        for i, carta in enumerate(self.cartas):
            lblCarta = Label(self, image=carta)
            lblCarta.grid(row=0, column=i)
