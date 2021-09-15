from tkinter import *
from os import path


class Fileira(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='white')
        self.imgCartas = [PhotoImage() for _ in range(5)]
        self.cartas = [Label(self, bg='white', cursor="hand2") for _ in range(5)]
        for i in range(5):
            self.cartas[i].grid(row=0, column=i)

    # Recebe atualização nas cartas da fileira
    def atualizarCartas(self, fileira):
        # Caminho relativo atual
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        for i in range(5):  # Redefine as imagens de cada label de acordo com a carta correspondente
            if i < len(fileira.cartas):
                self.imgCartas[i].configure(file=f"{pathName}/Views/img/cartas/{fileira.cartas[i].numero}.png")
                self.cartas[i].configure(image=self.imgCartas[i])
            else:   # Demais cartas não existem
                self.cartas[i].configure(image="")
            
