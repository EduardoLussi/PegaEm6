from tkinter import *
from os import path


class Placar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='white')

        # Ordem dos jogadores =====================
        # Caminho relativo atual
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.imgOrdemJogadores = PhotoImage(file=f"{pathName}/Views/img/ordemJogadores.png")
        self.lblOrdemJogadores = Label(self, image=self.imgOrdemJogadores)
        self.lblOrdemJogadores.configure(background="white")
        self.lblOrdemJogadores.pack(anchor=E, pady=15)

        # Jogador atual
        self.lblVez = Label(self, text="")
        self.lblVez.configure(font=("Century Gothic", 15),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblVez.pack(anchor=E)

        # Próximo jogador
        self.lblProxVez = Label(self, text="")
        self.lblProxVez.configure(font=("Century Gothic", 15),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblProxVez.pack(anchor=E)

        # Linha de divisão ======================
        self.frLinha = Frame(self, background='#ead215', height=3, width=500)
        self.frLinha.pack(anchor=E, pady=20)

        # Ranking dos jogadores ================
        self.imgClassificacao = PhotoImage(file=f"{pathName}/Views/img/classificacao.png")

        self.lblClassificacao = Label(self, image=self.imgClassificacao)
        self.lblClassificacao.configure(background="white")
        self.lblClassificacao.pack(anchor=E, pady=15)
        
        self.lblsJogador = []

        self.frRanking = Frame(self, bg='white')
        self.frRanking.pack(anchor=E)

        # Linha de divisão ====================
        self.frLinhaClassificacao = Frame(self, background='#ead215', height=3, width=500)
        self.frLinhaClassificacao.pack(anchor=E, pady=20)

        # Últimos lances ======================
        self.imgLances = PhotoImage(file=f"{pathName}/Views/img/ultimosLances.png")
        self.lbllances = Label(self, image=self.imgLances)
        self.lbllances.configure(background="white")
        self.lbllances.pack(anchor=E, pady=15)

        self.lblsLance = []

        self.frLances = Frame(self, bg='white')
        self.frLances.pack(anchor=E)

    # Recebe atualização dos lances
    def atualizarUltimosLances(self, lances):
        for lbl in self.lblsLance:  # Destrói labels dos lances existentes
            lbl.destroy()

        self.lblsLance = []
        for i in range(len(lances)):    # Cria novas labels para cada lance
            self.lblsLance.append(Label(self.frLances, text=f"{lances[i].jogador.nome}: Carta {lances[i].carta.numero}"))
            self.lblsLance[i].configure(font=("Century Gothic", 15),
                                 bg="white",
                                 fg="#0e6fb6")
            self.lblsLance[i].pack(anchor=E)
    
    # Recebe atualização no ranking
    def definirRanking(self, ranking):
        for lbl in self.lblsJogador:    # Destrói labels dos jogadores do ranking existentes
            lbl.destroy()

        self.lblsJogador = []
        for i in range(len(ranking)):   # Cria novas labels para cada jogador
            self.lblsJogador.append(Label(self.frRanking, text=f"{ranking[i].nome}: {ranking[i].pontuacao} pontos"))
            self.lblsJogador[i].configure(font=("Century Gothic", 15),
                                 bg="white",
                                 fg="#0e6fb6")
            self.lblsJogador[i].pack(anchor=E)