class Jogador:
    def __init__(self, nome="", mao=[], pontuacao=0):
        self.nome = nome
        self.mao = mao
        self.pontuacao = pontuacao

    def limpar(self):
        self.pontuacao = 0
        self.mao = []

    def removerCarta(self, carta):
        self.mao.remove(carta)
    
    # Métodos Get e Set ==========
    def getMao(self):
        return self.mao
    
    def setMao(self, mao):
        self.mao = mao

    def getPontuacao(self):
        return self.pontuacao
    
    def setPontuacao(self, pontuacao):
        self.pontuacao = pontuacao
    
    def setNome(self, nome):
        self.nome = nome