from tkinter import *


class Placar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='white')

        self.jogadores = [12, 31, 34]
        for i, jogador in enumerate(self.jogadores):
            lblJogador = Label(self, text=f"Jogador {i + 1}: {self.jogadores[i]} pontos")
            lblJogador.configure(font=("Century Gothic", 15),
                                 bg="white",
                                 fg="#0e6fb6")
            lblJogador.pack(anchor=E)
