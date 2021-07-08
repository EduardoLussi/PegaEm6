from tkinter import *
from os import path


class Fileira(Frame):
    def __init__(self, master, qtCartas=5):
        Frame.__init__(self, master=master)
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.cartas = [PhotoImage(file=f"{pathName}/img/cartas/9.png")] * qtCartas
        self.atualizarCartas()

    def atualizarCartas(self):
        for i, carta in enumerate(self.cartas):
            lblCarta = Label(self, image=carta, bg='white', cursor="hand2")
            lblCarta.bind("<Enter>", lblCarta.configure(fg="#ead215"))
            lblCarta.bind("<Leave>", lblCarta.configure(fg="white"))
            lblCarta.grid(row=0, column=i)
