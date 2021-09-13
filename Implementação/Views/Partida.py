from tkinter import *
from Views.Components.Mesa import Mesa
from Views.Components.Fileira import Fileira
from Views.Components.Placar import Placar
from Views.Resultado import Resultado
from Views.Components.Botao import Botao
from os import path


class Partida(Frame):
    def __init__(self, master, interface):
        self.master = master
        self.interface= interface

        Frame.__init__(self,
                       master=master,
                       width=self.master.winfo_screenwidth(),
                       height=self.master.winfo_screenheight(),
                       background="white")

        self.master.configure(background="white")
        self.master.state("zoomed")

        self.master.title("Mesa")

        self.frMesa = Mesa(self)
        self.frMesa.place(relx=0.03, rely=0.34, anchor=W)

        # Placar de informações
        self.placar = Placar(self)
        self.placar.place(relx=0.98, rely=0.3, anchor=E)

        self.frMao = Frame(self)
        self.imgCartasMao = []
        self.maoJogador = []
        self.frMao.place(relx=0.5, rely=0.82, anchor=CENTER)

        self.lblMessage = Label(self, text="Escolha sua carta")
        self.lblMessage.configure(font=("Century Gothic", 22),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblMessage.place(relx=0.5, rely=0.95, anchor=CENTER)

        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.imgRestart = PhotoImage(file=f"{pathName}/Views/img/refresh.png")
        self.lblRestart = Label(self, image=self.imgRestart, bg='white', cursor="hand2")
        self.lblRestart.bind("<Button-1>", self.restart)
        self.lblRestart.place(relx=0.04, rely=0.93, anchor=CENTER)

        self.pack()

    def atualizarModoMesa(self, modo):
        if modo:
            for child in self.frMao.winfo_children():
                child.configure(state="normal")
        else:
            for child in self.frMao.winfo_children():
                child.configure(state="disable")

    def atualizarFileirasMesa(self, fileiras):
        self.frMesa.atualizarFileirasMesa(fileiras)

    def definirJogadorAtualMesa(self, jogadorAtual):
        self.placar.lblVez.configure(text=f"Vez de {jogadorAtual.nome}")

    def definirProxJogadorMesa(self, proxJogador):
        self.placar.lblProxVez.configure(text=f"Próximo a jogar será {proxJogador.nome}")

    def restart(self, e):
        ...

    def escolherCarta(self, carta):
        self.interface.escolherCarta(carta)

    def definirCartasJogador(self, cartas):
        pathName = path.abspath(path.dirname('')).replace("\\", "/")

        self.imgCartasMao.clear()
        self.maoJogador.clear()
        for i in range(len(cartas)):
            self.imgCartasMao.append(PhotoImage(file=f"{pathName}/Views/img/cartas/{cartas[i].numero}.png"))
            self.maoJogador.append(Button(self.frMao,
                                          image=self.imgCartasMao[i],
                                          relief="solid",
                                          bd=0,
                                          activebackground="#ead215",
                                          bg="white",
                                          cursor="hand2",
                                          command=lambda carta=cartas[i]: self.escolherCarta(carta)))
            self.maoJogador[i].grid(row=0, column=i)
