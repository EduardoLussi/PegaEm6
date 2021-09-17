class Jogador:
    def __init__(self, nome="", mao=[], pontuacao=0):
        self.nome = nome
        self.mao = mao
        self.pontuacao = pontuacao

    def setNome(self, nome):
        self.nome = nome

    def limpar(self):
        self.pontuacao = 0
        self.mao = []