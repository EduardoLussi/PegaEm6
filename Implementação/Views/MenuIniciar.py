from tkinter import *
from Views.Components.Botao import Botao
from os import path


class MenuIniciar(Frame):
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

        self.master.title("Menu Iniciar")

        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.imagemTitulo = PhotoImage(file=f"{pathName}/Views/img/titulo.png")

        self.titulo = Label(self, image=self.imagemTitulo)
        self.titulo.configure(background="white")
        self.titulo.place(relx=0.5, rely=0.15, anchor=CENTER)

        self.frQtJogadores = Frame(self, bg="white")

        self.qtJogadoresTexto = Label(self.frQtJogadores, text="Escolha a quantidade de jogadores:")
        self.qtJogadoresTexto.configure(font=("Century Gothic", 30),
                                        bg="white",
                                        fg="#0e6fb6")
        self.qtJogadoresTexto.grid(row=0, column=0, padx=25)

        self.qtJogadoresEscala = Scale(self.frQtJogadores, from_=2, to=10, orient=HORIZONTAL)
        self.qtJogadoresEscala.configure(width=25,
                                         length=300,
                                         cursor="hand2",
                                         bg="#0e6fb6",
                                         fg="white",
                                         troughcolor="#E1DEDD",
                                         font=("Arial", 12))
        self.qtJogadoresEscala.grid(row=0, column=1, padx=25)

        self.frQtJogadores.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.botao = Botao(self, "Jogar", command=self.iniciarPartida)
        self.botao.place(relx=0.5, rely=0.85, anchor=CENTER)

        self.pack()

    def iniciarPartida(self):
        qtJogadores = self.qtJogadoresEscala.get()
        self.interface.iniciarPartida(qtJogadores)

