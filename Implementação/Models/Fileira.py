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
            pontuacao += carta.getPontuacao()
        return pontuacao
    
    # Métodos Get e Set
    def getCartas(self):
        return self.cartas

    def setCartas(self, cartas):
        self.cartas = cartas