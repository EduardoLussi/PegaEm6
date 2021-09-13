from tkinter import *
from os import path


class Placar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='white')
        pathName = path.abspath(path.dirname('')).replace("\\", "/")

        self.imgOrdemJogadores = PhotoImage(file=f"{pathName}/Views/img/ordemJogadores.png")

        self.lblOrdemJogadores = Label(self, image=self.imgOrdemJogadores)
        self.lblOrdemJogadores.configure(background="white")
        self.lblOrdemJogadores.pack(anchor=E, pady=15)

        self.lblVez = Label(self, text="")
        self.lblVez.configure(font=("Century Gothic", 15),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblVez.pack(anchor=E)

        self.lblProxVez = Label(self, text="")
        self.lblProxVez.configure(font=("Century Gothic", 15),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblProxVez.pack(anchor=E)

        self.frLinha = Frame(self, background='#ead215', height=3, width=500)
        self.frLinha.pack(anchor=E, pady=20)

        self.imgClassificacao = PhotoImage(file=f"{pathName}/Views/img/classificacao.png")

        self.lblClassificacao = Label(self, image=self.imgClassificacao)
        self.lblClassificacao.configure(background="white")
        self.lblClassificacao.pack(anchor=E, pady=15)

        self.jogadores = [12, 31, 34]
        for i in range(len(self.jogadores)):
            lblJogador = Label(self, text=f"Jogador {i + 1}: {self.jogadores[i]} pontos")
            lblJogador.configure(font=("Century Gothic", 15),
                                 bg="white",
                                 fg="#0e6fb6")
            lblJogador.pack(anchor=E)
        
        self.frLinhaClassificacao = Frame(self, background='#ead215', height=3, width=500)
        self.frLinhaClassificacao.pack(anchor=E, pady=20)

        self.imgLances = PhotoImage(file=f"{pathName}/Views/img/ultimosLances.png")

        self.lbllances = Label(self, image=self.imgLances)
        self.lbllances.configure(background="white")
        self.lbllances.pack(anchor=E, pady=15)

        self.lances = [12, 34, 1]
        for i in range(len(self.jogadores)):
            lblLance = Label(self, text=f"Jogador {i + 1}: Carta {self.lances[i]}")
            lblLance.configure(font=("Century Gothic", 15),
                                 bg="white",
                                 fg="#0e6fb6")
            lblLance.pack(anchor=E)

        