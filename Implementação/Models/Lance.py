class Lance:
    def __init__(self, carta=None, jogador=None):
        self.carta = carta
        self.jogador = jogador
    
    def getJogador(self):
        return self.jogador
    
    def getCarta(self):
        return self.carta