from tkinter import *
from Components.Botao import Botao


class MenuIniciar(Frame):
    def __init__(self, master, parent_root):
        self.parent_root = parent_root

        Frame.__init__(self,
                       master=master,
                       width=self.parent_root.winfo_screenwidth(),
                       height=self.parent_root.winfo_screenheight(),
                       background="white")

        self.master.configure(background="white")
        self.master.state("zoomed")

        self.master.title("Menu Inicial")

        self.imagemTitulo = PhotoImage(file="img/titulo.png")

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

        self.botao = Botao(self)
        self.botao.place(relx=0.5, rely=0.85, anchor=CENTER)

        self.pack()


if __name__ == '__main__':
    root = Tk()
    tela = MenuIniciar(root, root)
    root.mainloop()
