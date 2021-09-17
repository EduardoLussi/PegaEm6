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
        
    # Redistribui as cartas e envia as atualizações à interface
    def redistribuirCartas(self):
        self.mesa.redistribuirCartas()
        self.telaMesa.atualizarModoMesa(True)
        self.telaMesa.atualizarFileirasMesa(self.mesa.fileiras)

    # Redefine a partida, redistribui as cartas e atualiza as informações na interface
    def redefinirPartida(self):
        self.mesa.redefinirPartida()
        self.redistribuirCartas()
        self.telaIniciarLance.definirJogadorAtual(self.mesa.jogadorAtual)

        # Troca para a tela de iniciar lance
        self.mainWindow.withdraw()
        self.rootIniciarLance.state("zoomed")
        self.rootIniciarLance.deiconify()

    # Inicia uma nova partida e a redefine
    def iniciarPartida(self, qtJogadores):
        self.mesa.iniciarPartida(int(qtJogadores))
        self.redefinirPartida()
        
    # Prepara a tela do jogador atual
    def iniciarLance(self):
        # Atualiza informações da mesa para o jogador atual
        self.telaMesa.definirJogadorAtualMesa(self.mesa.jogadorAtual)
        self.telaMesa.definirProxJogadorMesa(self.mesa.obterProximoJogador())
        self.telaMesa.definirCartasJogador(self.mesa.jogadorAtual.mao)

        # Troca para a tela da mesa
        self.rootMesa.state("zoomed")
        self.rootMesa.deiconify()
        self.rootIniciarLance.withdraw()
    
    # Procedimento quando jogador escolhe uma carta
    def escolherCarta(self, carta):
        jogadorAtual = self.mesa.jogadorAtual

        self.mesa.incluirLance(Lance(carta, jogadorAtual))  # Inserção ordenada
        jogadorAtual.mao.remove(carta)

        ultimoJogador = self.mesa.ehUltimoJogador()

        if ultimoJogador:   # Fim do turno
            # Atualiza os últimos lances do placar da interface
            self.telaMesa.atualizarUltimosLances(self.mesa.lances)

            lanceInvalido = self.mesa.avaliarLances()
            
            # Atualza o ranking no placar da interface
            ranking = self.mesa.obterRanking()
            self.telaMesa.definirRanking(ranking)

            if self.telaIniciarLance.lblEditarNome is not None:
                self.telaIniciarLance.lblNomeJogador["state"] = "disabled"
                self.telaIniciarLance.lblEditarNome.destroy()
                self.telaIniciarLance.lblEditarNome = None
        
            if lanceInvalido:   # Necessária uma rodada de escolha de fileira
                self.mesa.jogadorAtual = lanceInvalido.jogador
                self.telaMesa.atualizarModoMesa(False)
            else:   # Todos os lances puderam ser inseridos
                # Atualiza fileiras da interface
                self.telaMesa.atualizarFileirasMesa(self.mesa.fileiras)
                self.mesa.definirProxJogador()

                if self.mesa.jogadorAtual.mao == []:    # Fim da rodada
                    if self.mesa.avaliarFimPartida():   # Fim da partida
                        self.telaResultado.definirRankingFinal(self.mesa.obterRanking())

                        # Troca para a tela de resultado
                        self.rootResultado.state("zoomed")
                        self.rootResultado.deiconify()
                        self.rootMesa.withdraw()
                        return
                    else:   # Partida ainda não acabou
                        self.mesa.redistribuirCartas()
                        self.telaMesa.atualizarFileirasMesa(self.mesa.fileiras)
        else:   # Turno ainda não acabou, há jogadores para escolherem cartas
            self.mesa.definirProxJogador()

        # Atualiza jogador atual na interface
        self.telaIniciarLance.definirJogadorAtual(self.mesa.jogadorAtual)

        # Troca para a tela de transição entre jogadores
        self.rootIniciarLance.state("zoomed")
        self.rootIniciarLance.deiconify()
        self.rootMesa.withdraw()

    # Fileira escolhida para ser substituída
    def redefinirFileira(self, fileira):
        self.mesa.redefinirFileira(fileira)

        self.telaMesa.atualizarModoMesa(True)   # Modo escolha de carta

        self.mesa.avaliarLances()   # Todos os demais lances são válidos
        
        self.telaMesa.definirRanking(self.mesa.obterRanking())

        self.mesa.jogadorAtual = self.mesa.jogadores[0] # Próximo jogador é o 1º da lista

        if self.mesa.jogadorAtual.mao == []:    # Fim da rodada
            if self.mesa.avaliarFimPartida():   # Fim da partida
                self.telaResultado.definirRankingFinal(self.mesa.obterRanking())

                # Troca para a tela de resultado
                self.rootResultado.state("zoomed")
                self.rootResultado.deiconify()
                self.rootMesa.withdraw()
                return
            else:   # Partida ainda não acabou
                self.mesa.redistribuirCartas()

        self.telaMesa.atualizarFileirasMesa(self.mesa.fileiras)

        self.telaIniciarLance.definirJogadorAtual(self.mesa.jogadorAtual)
        
        # Troca para a tela de transição entre jogadores
        self.rootIniciarLance.state("zoomed")
        self.rootIniciarLance.deiconify()
        self.rootMesa.withdraw()

    def alterarNome(self, nome):
        self.mesa.jogadorAtual.nome = nome

if __name__ == '__main__':
    AtorJogador()
