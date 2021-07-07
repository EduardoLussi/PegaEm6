from tkinter import *
from Components.Mesa import Mesa


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
        self.frMesa.pack()

        # self.master.withdraw() # Esconde root da tela atual
        # self.abrirTelaIniciarJogada()  # Chama a tela de iniciar jogada

    # def abrirTelaIniciarJogada(self):
    # root = Toplevel()  # Cria root da tela de iniciar jogada
    # IniciarJogada(root, self.master) # Cria tela de iniciar jogada


if __name__ == '__main__':
    root = Tk()
    mesa = Partida(root, root)
    root.mainloop()
