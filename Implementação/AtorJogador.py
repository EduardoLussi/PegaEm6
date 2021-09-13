from Models.Lance import Lance
from tkinter import *
from Views.MenuIniciar import MenuIniciar
from Views.IniciarLance import IniciarLance
from Views.Partida import Partida
from Views.Resultado import Resultado
from Models.Mesa import Mesa


class AtorJogador:

    def __init__(self):
        self.mesa = Mesa()

        self.mainWindow = Tk()
        self.telaMenuIniciar = MenuIniciar(self.mainWindow, self)
        
        # Tela Iniciar Lance
        self.rootIniciarLance = Toplevel(self.mainWindow)
        self.rootIniciarLance.protocol("WM_DELETE_WINDOW", self.mainWindow.destroy)
        self.telaIniciarLance = IniciarLance(self.rootIniciarLance, self)
        self.rootIniciarLance.withdraw()

        # Tela Partida
        self.rootMesa = Toplevel(self.mainWindow)
        self.rootMesa.protocol("WM_DELETE_WINDOW", self.mainWindow.destroy)
        self.telaMesa = Partida(self.rootMesa, self)
        self.rootMesa.withdraw()

        # Tela Resultado
        self.rootResultado = Toplevel(self.mainWindow)
        self.rootResultado.protocol("WM_DELETE_WINDOW", self.mainWindow.destroy)
        self.telaResultado = Resultado(self.rootResultado, self)
        self.rootResultado.withdraw()

        self.mainWindow.protocol("WM_DELETE_WINDOW", self.mainWindow.destroy)
        self.mainWindow.mainloop()
        

    def redistribuirCartas(self):
        self.mesa.redistribuirCartas()

        self.telaMesa.atualizarModoMesa(True)
        self.telaMesa.atualizarFileirasMesa(self.mesa.fileiras)

    def redefinirPartida(self):
        self.mesa.redefinirPartida()
        self.redistribuirCartas()
        self.telaIniciarLance.definirJogadorAtual(self.mesa.jogadorAtual)
        self.mainWindow.withdraw()
        self.rootIniciarLance.state("zoomed")
        self.rootIniciarLance.deiconify()

    def iniciarPartida(self, qtJogadores):
        self.mesa.iniciarPartida(int(qtJogadores))
        self.redefinirPartida()
        

    def iniciarLance(self):
        self.telaMesa.definirJogadorAtualMesa(self.mesa.jogadorAtual)
        self.telaMesa.definirProxJogadorMesa(self.mesa.obterProximoJogador())
        self.telaMesa.definirCartasJogador(self.mesa.jogadorAtual.mao)

        self.rootMesa.state("zoomed")
        self.rootMesa.deiconify()
        self.rootIniciarLance.withdraw()
    
    def escolherCarta(self, carta):
        jogadorAtual = self.mesa.jogadorAtual

        self.mesa.incluirLance(Lance(carta, jogadorAtual))
        jogadorAtual.mao.remove(carta)

        ultimoJogador = self.mesa.ehUltimoJogador()

        if ultimoJogador:
            ...# Falta essa parte
        else:
            self.mesa.definirProxJogador()

        jogadorAtual = self.mesa.jogadorAtual
        self.telaIniciarLance.definirJogadorAtual(jogadorAtual)

        self.rootIniciarLance.state("zoomed")
        self.rootIniciarLance.deiconify()
        self.rootMesa.withdraw()


if __name__ == '__main__':
    AtorJogador()
