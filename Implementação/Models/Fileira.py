class Fileira:
    def __init__(self, cartas=[]):
        self.cartas = cartas
    
    def limpar(self):
        self.cartas.clear()
    
    def inserirCarta(self, carta):
        self.cartas.append(carta)
    
    def obterPontuacao(self):
        pontuacao = 0
        for carta in self.cartas:
            pontuacao += carta.pontuacao
        return pontuacao