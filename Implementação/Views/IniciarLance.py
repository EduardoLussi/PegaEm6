from tkinter import *
from Views.Components.Botao import Botao
from Views.Partida import Partida
from os import path


class IniciarLance(Frame):
    def __init__(self, master, interface):
        self.interface = interface
        self.master = master

        Frame.__init__(self,
                       master=master,
                       width=self.master.winfo_screenwidth(),
                       height=self.master.winfo_screenheight(),
                       background="white")

        self.master.configure(background="white")
        self.master.state("zoomed")

        self.master.title("Iniciar Jogada")

        # Título principal: Jogador da vez ==============================
        self.frVez = Frame(self, bg='white')

        self.lblNomeJogador = Button(self.frVez)
        self.lblNomeJogador.configure(font=("Century Gothic", 80),
                                        bg="white",
                                        fg="#0e6fb6",
                                        relief="solid",
                                        bd=0,
                                        cursor="hand2",
                                        text="Vez de ",
                                        command=self.mostrarEntradaNome)
        self.lblNomeJogador.grid(row=0, column=1)

        self.frVez.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Label que informa possibilidade de edição de nome ============
        self.lblEditarNome = Label(self, text=f'Você pode editar seu nome clicando em Vez de')
        self.lblEditarNome.configure(font=("Century Gothic", 15),
                                     bg="white",
                                     fg="#0e6fb6")
        self.lblEditarNome.place(relx=0.98, rely=0.97, anchor=SE)

        # Botão de iniciar lance ======================================
        self.botao = Botao(self, "Continuar", command=self.iniciarLance)
        self.botao.place(relx=0.5, rely=0.85, anchor=CENTER)

        # Botão de reiniciar ==========================================
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        self.imgRestart = PhotoImage(file=f"{pathName}/Views/img/refresh.png")
        self.lblRestart = Label(self, image=self.imgRestart, bg='white', cursor="hand2")
        self.lblRestart.bind("<Button-1>", self.reiniciar)
        self.lblRestart.place(relx=0.04, rely=0.93, anchor=CENTER)

        self.lblInserirNome = None

        self.pack()

    def reiniciar(self, e):
        if self.lblInserirNome is not None:
            self.novoNome.delete(0, 'end')
            self.novoNome.destroy()
            self.botaoEntrada.destroy()
            self.lblInserirNome.destroy()
            self.lblInserirNome = None
        self.interface.telaMesa.reiniciar(None)

    # Recebe atualização do jogador atual
    def definirJogadorAtual(self, jogador):
        self.lblNomeJogador.configure(text=f"Vez de {jogador.nome}")
        if self.lblEditarNome is not None:
            self.lblEditarNome.configure(text=f'Você pode editar seu nome clicando em Vez de {jogador.nome}')

    # Inicia o lance
    def iniciarLance(self):
        if self.lblInserirNome is not None:
            self.novoNome.delete(0, 'end')
            self.novoNome.destroy()
            self.botaoEntrada.destroy()
            self.lblInserirNome.destroy()
            self.lblInserirNome = None
        self.interface.iniciarLance()

    # Mostra campos para alterar o nome do jogador atual
    def mostrarEntradaNome(self):
        self.lblInserirNome = Label(self, text="Insira o novo nome:")
        self.lblInserirNome.configure(font=("Century Gothic", 16),
                                  bg="white",
                                  fg="#0e6fb6")
        self.lblInserirNome.place(relx=0.45, rely=0.6, anchor=CENTER)

        self.novoNome = Entry(self, text="Insira o seu novo nome:")
        self.novoNome.configure(font=("Century Gothic", 16),
                               width=30,
                               bg="lightgray")
        self.novoNome.place(relx=0.65, rely=0.6, anchor=CENTER)

        self.botaoEntrada = Botao(self, "Ok", command=self.alterarNome)
        self.botaoEntrada.place(relx=0.82, rely=0.6, anchor=CENTER)

    # Envia requisição de atualização do nome do jogador
    def alterarNome(self):
        self.lblInserirNome.destroy()
        self.lblInserirNome = None
        self.interface.alterarNome(self.novoNome.get())
        self.lblNomeJogador.configure(text=f"Vez de {self.novoNome.get()}")
        self.lblEditarNome.configure(text=f"Você pode editar seu nome clicando em Vez de {self.novoNome.get()}")
        self.novoNome.delete(0, 'end')
        self.novoNome.destroy()
        self.botaoEntrada.destroy()

