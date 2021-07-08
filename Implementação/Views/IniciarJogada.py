from tkinter import *
from Components.Botao import Botao


class IniciarJogada(Frame):
    def __init__(self, master, parent_root):
        self.parent_root = parent_root

        Frame.__init__(self,
                       master=master,
                       width=self.parent_root.winfo_screenwidth(),
                       height=self.parent_root.winfo_screenheight(),
                       background="white")

        self.master.configure(background="white")
        self.master.state("zoomed")

        self.master.title("Iniciar Jogada")

        self.frVez = Frame(self, bg='white')

        self.lblVez = Label(self.frVez, text="Vez de ")
        self.lblVez.configure(font=("Century Gothic", 80),
                              bg="white",
                              fg="#0e6fb6")
        self.lblVez.grid(row=0, column=0)

        self.nomeJogador = StringVar()
        self.nomeJogador.set("Jogador 1")

        self.lblNomeJogador = Label(self.frVez)
        self.lblNomeJogador.configure(font=("Century Gothic", 80),
                                        bg="white",
                                        fg="#0e6fb6",
                                        relief="solid",
                                        bd=0,
                                        cursor="hand2",
                                        textvariable=self.nomeJogador)
        self.lblNomeJogador.grid(row=0, column=1)

        self.frVez.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.lblEditarNome = Label(self, text=f'Você pode editar seu nome clicando em "{self.nomeJogador.get()}"')
        self.lblEditarNome.configure(font=("Century Gothic", 15),
                                     bg="white",
                                     fg="#0e6fb6")
        self.lblEditarNome.place(relx=0.15, rely=0.97, anchor=CENTER)

        self.botao = Botao(self)
        self.botao.place(relx=0.5, rely=0.85, anchor=CENTER)

        self.pack()


if __name__ == '__main__':
    root = Tk()
    tela = IniciarJogada(root, root)
    root.mainloop()
