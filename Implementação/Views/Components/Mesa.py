from tkinter import *
from Views.Components.Fileira import Fileira


class Mesa(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='white')
        self.fileiras = []

        for i in range(4):
            fileira = Fileira(self)
            self.fileiras.append(fileira)
            fileira.grid(row=i, column=0, sticky='w')

    # Recebe atualização nas fileiras
    def atualizarFileirasMesa(self, fileiras):
        for i, fileira in enumerate(self.fileiras):
            fileira.atualizarCartas(fileiras[i])
    
    # Recebe instrução para esconder botões de escolha de fileira
    def esconderEscolhaFileira(self):
        for fileira in self.fileiras:
            fileira.esconderEscolhaFileira()

    # Recebe instrução para mostrar botões de escolha de fileira
    def mostrarEscolhaFileira(self):
        for fileira in self.fileiras:
            fileira.mostrarEscolhaFileira()
    
    # Define qual fileira foi escolhida
    def redefinirFileira(self, fileira):
        self.master.redefinirFileira(self.fileiras.index(fileira))