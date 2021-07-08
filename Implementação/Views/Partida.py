from tkinter import *
from Views.Components.Mesa import Mesa
from Views.Components.Fileira import Fileira
from Views.Components.Placar import Placar
from Views.Resultado import Resultado
from os import path


class Partida(Frame):
    def __init__(self, master, parent_root, mainRoot):
        self.parent_root = parent_root
        self.mainRoot = mainRoot

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

        self.frVez = Frame(self, bg='white')

        self.lblVez = Label(self.frVez, text="Vez de jogador 1")
        self.lblVez.configure(font=("Century Gothic", 20),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblVez.pack(anchor=E)

        self.lblProxVez = Label(self.frVez, text="Próximo a jogar será Jogador 2")
        self.lblProxVez.configure(font=("Century Gothic", 20),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblProxVez.pack(anchor=E)

        self.frLinha = Frame(self.frVez, background='#ead215', height=3, width=500)
        self.frLinha.pack(anchor=E, pady=20)

        self.frVez.place(relx=0.85, rely=0.09, anchor=CENTER)

        self.placar = Placar(self)
        self.placar.place(relx=0.98, rely=0.3, anchor=E)

        self.frMao = Fileira(self, 10)
        self.frMao.bind("<Button-1>", self.jogarCarta)
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

    def restart(self, e):
        self.mainRoot.deiconify()
        self.master.withdraw()

    def jogarCarta(self, e):
        rootResultado = Toplevel()
        rootResultado.protocol("WM_DELETE_WINDOW", self.mainRoot)
        Resultado(rootResultado, self.master)
        self.master.withdraw()
