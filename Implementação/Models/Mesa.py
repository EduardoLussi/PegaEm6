from Models.Carta import Carta
from Models.Fileira import Fileira
from Models.Jogador import Jogador
from random import shuffle


class Mesa:
    def __init__(self, monte=[], fileiras=[Fileira() for _ in range(4)], jogadores=[], lances=[], jogadorAtual=None, modo=True):
        self.monte = monte
        self.fileiras = fileiras
        self.jogadores = jogadores
        self.lances = lances
        self.jogadorAtual = jogadorAtual
        self.modo = modo
    
    def iniciarPartida(self, qtJogadores):
        self.jogadores = [Jogador(f"Jogador {i+1}") for i in range(qtJogadores)]
    
    def redefinirPartida(self):
        for jogador in self.jogadores:
            jogador.limpar()

    def obterNovoBaralho(self):
        baralho = []
        for i in range(1, 105):
            pontuacao = 1
        
            if i == 55:
                pontuacao = 7
                baralho.append(Carta(i, pontuacao))
                continue
        
            if i % 5 == 0:
                pontuacao += 1
        
            if i % 10 == 0:
                pontuacao += 1
            
            if i % 11 == 0:
                pontuacao += 4
            
            baralho.append(Carta(i, pontuacao))

        shuffle(baralho)
        return baralho

    def redistribuirCartas(self):
        self.lances = []
        self.monte = self.obterNovoBaralho()
        
        for fileira in self.fileiras:
            fileira.cartas = [self.monte.pop(0)]
        
        for jogador in self.jogadores:
            jogador.mao = self.monte[:10]
            del self.monte[:10]
        
        self.jogadorAtual = self.jogadores[0]
        
    def obterProximoJogador(self):
        i = (self.jogadores.index(self.jogadorAtual) + 1) % len(self.jogadores)
        return self.jogadores[i]
        