from tkinter import *
from Components.Fileira import Fileira


class Mesa(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.fileiras = []

        for i in range(4):
            fileira = Fileira(self)
            self.fileiras.append(fileira)
            fileira.grid(row=i, column=0)

