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
        self.telaMesa.atualizarModoMesa(True)   # Modo escolha de carta
        
        fileiras = self.mesa.getFileiras()
        self.telaMesa.atualizarFileirasMesa(fileiras)

    # Redefine a partida, redistribui as cartas e atualiza as informações na interface
    def redefinirPartida(self):
        self.mesa.redefinirPartida()
        self.redistribuirCartas()

        jogadorAtual = self.mesa.getJogadorAtual()
        self.telaIniciarLance.definirJogadorAtual(jogadorAtual)

        self.telaMesa.definirRanking([])
        self.telaMesa.atualizarUltimosLances([])

        # Troca para a tela de iniciar lance
        self.mostrarTelaIniciarLance(self.mainWindow)

    # Inicia uma nova partida e a redefine
    def iniciarPartida(self, qtJogadores):
        self.mesa.iniciarPartida(int(qtJogadores))
        self.redefinirPartida()
        self.telaIniciarLance.habilitarAlterarNome()
        
    # Prepara a tela do jogador atual
    def iniciarLance(self):
        # Atualiza informações da mesa para o jogador atual
        jogadorAtual = self.mesa.getJogadorAtual()
        self.telaMesa.definirJogadorAtualMesa(jogadorAtual)

        proxJogador = self.mesa.obterProximoJogador()
        self.telaMesa.definirProxJogadorMesa(proxJogador)

        mao = jogadorAtual.getMao()
        self.telaMesa.definirCartasJogador(mao)

        # Troca para a tela da mesa
        self.mostrarTelaPartida(self.rootIniciarLance)
    
    # Procedimento quando jogador escolhe uma carta
    def escolherCarta(self, carta):
        jogadorAtual = self.mesa.getJogadorAtual()

        self.mesa.incluirLance(Lance(carta, jogadorAtual))  # Inserção ordenada
        jogadorAtual.removerCarta(carta)

        ultimoJogador = self.mesa.ehUltimoJogador()

        if ultimoJogador:   # Fim do turno
            # Atualiza os últimos lances do placar da interface
            lances = self.mesa.getLances()
            self.telaMesa.atualizarUltimosLances(lances)

            lanceInvalido = self.mesa.avaliarLances()
            
            # Atualza o ranking no placar da interface
            ranking = self.mesa.obterRanking()
            self.telaMesa.definirRanking(ranking)

            self.telaIniciarLance.desabilitarAlterarNome()
        
            if lanceInvalido:   # Necessária uma rodada de escolha de fileira
                jogadorLanceInvalido = lanceInvalido.getJogador()
                self.mesa.setJogadorAtual(jogadorLanceInvalido)
                self.telaMesa.atualizarModoMesa(False)
            else:   # Todos os lances puderam ser inseridos
                # Atualiza fileiras da interface
                fileiras = self.mesa.getFileiras()
                self.telaMesa.atualizarFileirasMesa(fileiras)

                self.mesa.definirProxJogador()

                jogadorAtual = self.mesa.getJogadorAtual()
                mao = jogadorAtual.getMao()
                if mao == []:    # Fim da rodada
                    if self.mesa.avaliarFimPartida():   # Fim da partida
                        self.telaResultado.definirRankingFinal(self.mesa.obterRanking())
                        self.mostrarTelaResultado(self.rootMesa)
                        return
                    else:   # Partida ainda não acabou
                        self.mesa.redistribuirCartas()
                        fileiras = self.mesa.getFileiras()
                        self.telaMesa.atualizarFileirasMesa(fileiras)
        else:   # Turno ainda não acabou, há jogadores para escolherem cartas
            self.mesa.definirProxJogador()

        # Atualiza jogador atual na interface
        jogadorAtual = self.mesa.getJogadorAtual()
        self.telaIniciarLance.definirJogadorAtual(jogadorAtual)

        # Troca para a tela de transição entre jogadores
        self.mostrarTelaIniciarLance(self.rootMesa)
        

    # Fileira escolhida para ser substituída
    def redefinirFileira(self, fileira):
        self.mesa.redefinirFileira(fileira)

        self.telaMesa.atualizarModoMesa(True)   # Modo escolha de carta

        self.mesa.avaliarLances()   # Todos os demais lances são válidos
        
        self.telaMesa.definirRanking(self.mesa.obterRanking())

        jogadoresMesa = self.mesa.getJogadores()
        self.mesa.setJogadorAtual(jogadoresMesa[0]) # Próximo jogador é o 1º da lista

        jogadorAtual = self.mesa.getJogadorAtual()
        mao = jogadorAtual.getMao()
        if mao == []:    # Fim da rodada
            if self.mesa.avaliarFimPartida():   # Fim da partida
                self.telaResultado.definirRankingFinal(self.mesa.obterRanking())
                self.mostrarTelaResultado(self.rootMesa)
                return
            else:   # Partida ainda não acabou
                self.mesa.redistribuirCartas()
        
        fileiras = self.mesa.getFileiras()
        self.telaMesa.atualizarFileirasMesa(fileiras)

        jogadorAtual = self.mesa.getJogadorAtual()
        self.telaIniciarLance.definirJogadorAtual(jogadorAtual)
        
        # Troca para a tela de transição entre jogadores
        self.mostrarTelaIniciarLance(self.rootMesa)

    def alterarNome(self, nome):
        jogadorAtual = self.mesa.getJogadorAtual()
        jogadorAtual.setNome(nome)

    def reiniciar(self, rootTela, redefinir):
        if redefinir is not None:
            if redefinir:
                self.mostrarTelaInicial(rootTela)
            elif not redefinir:
                rootTela.withdraw()
                self.redefinirPartida()

    # Trocas de tela ==============================

    def mostrarTelaInicial(self, rootTela):
        self.mainWindow.state("zoomed")
        self.mainWindow.deiconify()
        rootTela.withdraw()

    def mostrarTelaResultado(self, rootTela):
        self.rootResultado.state("zoomed")
        self.rootResultado.deiconify()
        rootTela.withdraw()
    
    def mostrarTelaIniciarLance(self, rootTela):
        self.rootIniciarLance.state("zoomed")
        self.rootIniciarLance.deiconify()
        rootTela.withdraw()

    def mostrarTelaPartida(self, rootTela):
        self.rootMesa.state("zoomed")
        self.rootMesa.deiconify()
        rootTela.withdraw()


if __name__ == '__main__':
    AtorJogador()
