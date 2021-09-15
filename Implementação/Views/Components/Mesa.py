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