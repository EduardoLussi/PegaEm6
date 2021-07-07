from tkinter import *


class IniciarJogada(Frame):
    def __init__(self, master, parent_root=None):
        Frame.__init__(self, master=master)

        self.parent_root = parent_root    # Root do pai

        self.master.title("Iniciar Jogada")
        self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}")
        self.master.state('zoomed')

        self.pack()


if __name__ == '__main__':
    root = Tk()
    mesa = IniciarJogada(root)
    root.mainloop()
