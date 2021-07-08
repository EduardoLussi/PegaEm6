from tkinter import *
from Components.Mesa import Mesa
from Components.Fileira import Fileira


class Partida(Frame):
    def __init__(self, master, parent_root):
        self.parent_root = parent_root

        Frame.__init__(self,
                       master=master,
                       width=self.parent_root.winfo_screenwidth(),
                       height=self.parent_root.winfo_screenheight(),
                       background="white")

        self.master.configure(background="white")
        self.master.state("zoomed")

        self.master.title("Mesa")

        self.frMesa = Mesa(self)
        self.frMesa.place(relx=0.16, rely=0.34, anchor=CENTER)

        self.frPlacar = Frame(self, bg='white')

        self.lblVez = Label(self.frPlacar, text="Vez de jogador 1")
        self.lblVez.configure(font=("Century Gothic", 20),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblVez.pack(anchor=E)

        self.lblProxVez = Label(self.frPlacar, text="Próximo a jogar será Jogador 2")
        self.lblProxVez.configure(font=("Century Gothic", 20),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblProxVez.pack(anchor=E)

        self.frLinha = Frame(self.frPlacar, background='#ead215', height=3, width=500)
        self.frLinha.pack(anchor=E, pady=20)

        self.jogadores = [12, 31, 34]
        for i, jogador in enumerate(self.jogadores):
            lblJogador = Label(self.frPlacar, text=f"Jogador {i+1}: {self.jogadores[i]} pontos")
            lblJogador.configure(font=("Century Gothic", 15),
                                  bg="white",
                                  fg="#0e6fb6")
            lblJogador.pack(anchor=E)

        self.frPlacar.place(relx=0.85, rely=0.13, anchor=CENTER)

        self.frMao = Fileira(self, 10)
        self.frMao.place(relx=0.5, rely=0.82, anchor=CENTER)

        self.lblMessage = Label(self, text="Escolha sua carta")
        self.lblMessage.configure(font=("Century Gothic", 22),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblMessage.place(relx=0.5, rely=0.95, anchor=CENTER)

        self.imgRestart = PhotoImage(file="img/refresh.png")
        self.lblRestart = Label(self, image=self.imgRestart, bg='white', cursor="hand2")
        self.lblRestart.place(relx=0.04, rely=0.93, anchor=CENTER)

        # self.master.withdraw() # Esconde root da tela atual
        # self.abrirTelaIniciarJogada()  # Chama a tela de iniciar jogada

        self.pack()

    # def abrirTelaIniciarJogada(self):
    # root = Toplevel()  # Cria root da tela de iniciar jogada
    # IniciarJogada(root, self.master) # Cria tela de iniciar jogada


if __name__ == '__main__':
    root = Tk()
    mesa = Partida(root, root)
    root.mainloop()
