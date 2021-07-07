from tkinter import *


class Mesa(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.btnJogarCarta = Button(self,
                                  text='Jogar Carta',
                                  padx=15,
                                  pady=5,
                                  font='Verdana 12',
                                  bg='white',
                                  bd='1',
                                  highlightbackground='black',
                                  relief='solid')
        self.btnJogarCarta.pack()

        self.pack()

        #self.master.withdraw() # Esconde root da tela atual
        #self.abrirTelaIniciarJogada()  # Chama a tela de iniciar jogada

    #def abrirTelaIniciarJogada(self):
        #root = Toplevel()  # Cria root da tela de iniciar jogada
        #IniciarJogada(root, self.master) # Cria tela de iniciar jogada


if __name__ == '__main__':
    root = Tk()
    root.title("Mesa")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.state('zoomed')
    mesa = Mesa(root)
    root.mainloop()
