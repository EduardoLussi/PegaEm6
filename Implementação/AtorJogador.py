from tkinter import *
from Views.MenuIniciar import MenuIniciar


class AtorJogador:

    def __init__(self):
        self.mainWindow = Tk()
        self.tela = MenuIniciar(self.mainWindow, self.mainWindow, self.mainWindow)
        self.mainWindow.protocol("WM_DELETE_WINDOW", self.mainWindow.destroy)
        self.mainWindow.mainloop()


if __name__ == '__main__':
    AtorJogador()
