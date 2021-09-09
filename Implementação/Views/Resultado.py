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
        self.lblVencedor.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.placar = Placar(self)
        self.placar.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.botao = Botao(self, "Menu Principal", command=self.reiniciar)
        self.botao.place(relx=0.5, rely=0.85, anchor=CENTER)

        self.pack()

    def reiniciar(self):
        ...
