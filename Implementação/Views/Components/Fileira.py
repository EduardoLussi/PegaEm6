from tkinter import *
from os import path


class Fileira(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='white')
        
        self.frameBtnFileira = Frame(self, highlightbackground="#0e6fb6", highlightthickness=4, bd=0)
        self.btnFileira = Button(self.frameBtnFileira, height=8, width=5, 
                                 cursor="hand2", relief="solid", 
                                 bg="#ee1934", bd=0, activebackground="#ead215",
                                 command=self.redefinirFileira)
        self.btnFileira.pack()
        self.frameBtnFileira.grid(row=0, column=0, padx=15)

        self.imgCartas = [PhotoImage() for _ in range(5)]
        self.cartas = [Label(self, bg='white') for _ in range(5)]
        for i in range(5):
            self.cartas[i].grid(row=0, column=i+1)

    # Recebe atualização nas cartas da fileira
    def atualizarCartas(self, fileira):
        # Caminho relativo atual
        pathName = path.abspath(path.dirname('')).replace("\\", "/")
        for i in range(5):  # Redefine as imagens de cada label de acordo com a carta correspondente
            if i < len(fileira.cartas):
                self.imgCartas[i].configure(file=f"{pathName}/Views/img/cartas/{fileira.cartas[i].numero}.png")
                self.cartas[i].configure(image=self.imgCartas[i])
            else:   # Demais cartas não existem
                self.cartas[i].configure(image="")
    
    # Escolha de fileira feita
    def redefinirFileira(self):
        self.master.redefinirFileira(self)

    # Esconde botão de escolha de fileira
    def esconderEscolhaFileira(self):
        self.frameBtnFileira.grid_forget()
    
    # Mostra botão de escolha de fileira
    def mostrarEscolhaFileira(self):
        self.frameBtnFileira.grid(row=0, column=0, padx=15)