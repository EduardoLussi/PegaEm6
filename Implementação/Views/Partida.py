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

        # Fileiras ===========================
        self.frMesa = Mesa(self)
        self.frMesa.place(relx=0.03, rely=0.34, anchor=W)

        # Placar de informações ==============
        self.placar = Placar(self)
        self.placar.place(relx=0.98, rely=0.03, anchor=NE)

        # Mão do Jogador =====================
        self.frMao = Frame(self)
        self.imgCartasMao = [PhotoImage() for _ in range(10)]
        self.maoJogador = [Button(self.frMao,
                                  relief="solid",
                                  bd=0,
                                  activebackground="#ead215",
                                  bg="white",
                                  cursor="hand2") for _ in range(10)]
        self.frMao.place(relx=0.5, rely=0.82, anchor=CENTER)

        # Mensagem de ação do jogador ========
        self.lblMessage = Label(self, text="Escolha uma carta")
        self.lblMessage.configure(font=("Century Gothic", 22),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblMessage.place(relx=0.5, rely=0.95, anchor=CENTER)

        # Botão de reiniciar ================
        # Caminho relativo atual
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.imgRestart = PhotoImage(file=f"{pathName}/Views/img/refresh.png")
        self.lblRestart = Label(self, image=self.imgRestart, bg='white', cursor="hand2")
        self.lblRestart.bind("<Button-1>", self.restart)
        self.lblRestart.place(relx=0.04, rely=0.93, anchor=CENTER)

        self.pack()

    # Recebe atualização do modo da mesa (Escolha de carta ou fileira)
    def atualizarModoMesa(self, modo):
        if modo:    # Modo escolha de carta
            self.frMesa.esconderEscolhaFileira()    # Esconde botões de escolha de fileira
            for i in range(len(self.maoJogador)):   # Ativa botões das cartas
                self.maoJogador[i].configure(state=NORMAL)
            # Muda mensagem para escolha de carta
            self.lblMessage.configure(text="Escolha uma carta")
        else:
            self.frMesa.mostrarEscolhaFileira() # Mostra botões de escolha de fileira
            for i in range(len(self.maoJogador)):   # Desativa botões das cartas
                self.maoJogador[i].configure(state=DISABLED)
            # Muda mensagem para escolha de carta
            self.lblMessage.configure(text="Escolha uma fileira")

    # Recebe atualização das fileiras da mesa
    def atualizarFileirasMesa(self, fileiras):
        self.frMesa.atualizarFileirasMesa(fileiras)

    # Recebe atualização do jogador atual da mesa
    def definirJogadorAtualMesa(self, jogadorAtual):
        self.placar.lblVez.configure(text=f"Vez de {jogadorAtual.nome}")

    # Recebe atualização do próximo jogador
    def definirProxJogadorMesa(self, proxJogador):
        self.placar.lblProxVez.configure(text=f"Próximo a jogar será {proxJogador.nome}")

    def restart(self, e):
        ...

    # Envia carta escolhida
    def escolherCarta(self, carta):
        self.interface.escolherCarta(carta)

    # Recebe nova mão do jogador
    def definirCartasJogador(self, cartas):
        # Caminho relativo atual
        pathName = path.abspath(path.dirname('')).replace("\\", "/")

        for i in range(10):
            if i < len(cartas):
                self.imgCartasMao[i].configure(file=f"{pathName}/Views/img/cartas/{cartas[i].numero}.png")
                self.maoJogador[i].configure(image=self.imgCartasMao[i],
                                            command=lambda carta=cartas[i]: self.escolherCarta(carta))
                self.maoJogador[i].grid(row=0, column=i)
            else:
                self.maoJogador[i].grid_forget()

    # Recebe atualização dos últimos lances do placar
    def atualizarUltimosLances(self, lances):
        self.placar.atualizarUltimosLances(lances)
    
    # Recebe atualização no ranking do placar
    def definirRanking(self, ranking):
        self.placar.definirRanking(ranking)
    
    # Redefine fileira
    def redefinirFileira(self, i):
        self.interface.redefinirFileira(i)