from tkinter import *
from Views.MenuIniciar import MenuIniciar


def abrirJogo():
    root = Tk()
    tela = MenuIniciar(root, root, root)
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()


if __name__ == '__main__':
    abrirJogo()
