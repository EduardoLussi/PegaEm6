from tkinter import *
from Views.Components.Botao import Botao
from Views.Components.Placar import Placar
from os import path


class Resultado(Frame):
    def __init__(self, master, interface):
        self.master = master
        self.interface = interface

        Frame.__init__(self,
                       master=self.master,
                       width=self.master.winfo_screenwidth(),
                       height=self.master.winfo_screenheight(),
                       background="white")

        self.master.configure(background="white")
        self.master.state("zoomed")

        self.master.title("Menu Inicial")

        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.imagemTitulo = PhotoImage(file=f"{pathName}/Views/img/titulo.png")

        self.titulo = Label(self, image=self.imagemTitulo)
        self.titulo.configure(background="white")
        self.titulo.place(relx=0.5, rely=0.15, anchor=CENTER)

        self.lblVencedor = Label(self, text="Jogador 1 venceu a partida!")
        self.lblVencedor.configure(font=("Century Gothic", 35),
                                        bg="white",
                                        fg="#0e6fb6")
        self.lblVencedor.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.lblsJogador = []

        self.frRanking = Frame(self, bg='white')

        self.imgClassificacao = PhotoImage(file=f"{pathName}/Views/img/classificacao.png")
        self.lblClassificacao = Label(self.frRanking, image=self.imgClassificacao, bg="white")
        self.lblClassificacao.pack(anchor=E, pady=10)

        self.frRanking.place(anchor=NE, relx=0.98, rely=0.37)

        self.botao = Botao(self, "Menu Principal", command=self.reiniciar)
        self.botao.place(relx=0.5, rely=0.85, anchor=CENTER)

        self.pack()

    def reiniciar(self):
        ...

    def definirRankingFinal(self, ranking):
        self.lblVencedor.configure(text=f"{ranking[0].nome} venceu a partida!")

        for lbl in self.lblsJogador:    # Destrói labels dos jogadores do ranking existentes
            lbl.destroy()

        self.lblsJogador = []
        for i in range(len(ranking)):   # Cria novas labels para cada jogador
            self.lblsJogador.append(Label(self.frRanking, text=f"{ranking[i].nome}: {ranking[i].pontuacao} pontos"))
            self.lblsJogador[i].configure(font=("Century Gothic", 15),
                                 bg="white",
                                 fg="#0e6fb6")
            self.lblsJogador[i].pack(anchor=E)