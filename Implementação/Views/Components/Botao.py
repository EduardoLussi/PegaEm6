from tkinter import *


class Botao(Frame):
    def __init__(self, master, command=None, text="Jogar"):
        Frame.__init__(self, master=master)

        self.configure(highlightbackground="#0e6fb6",
                       highlightcolor="#0e6fb6",
                       highlightthickness=4,
                       bd=0)

        self.jogar = Button(self, text=text, command=command)
        self.jogar.configure(padx=15,
                             height=1,
                             cursor="hand2",
                             fg="#0e6fb6",
                             bg="#ead215",
                             font=("Century Gothic", 28),
                             relief="solid",
                             bd=0,
                             activebackground="#efe387",
                             activeforeground="#4c8ebd")

        self.jogar.pack()
