from tkinter import *
from os import path


class Fileira(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='white')
        self.imgCartas = [PhotoImage() for _ in range(5)]
        self.cartas = [Label(self, bg='white', cursor="hand2") for _ in range(5)]
        for i in range(5):
            self.cartas[i].grid(row=0, column=i)

    def atualizarCartas(self, fileira):
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        for i, carta in enumerate(fileira.cartas):
            self.imgCartas[i].configure(file=f"{pathName}/Views/img/cartas/{carta.numero}.png")
            self.cartas[i].configure(image=self.imgCartas[i])
            
