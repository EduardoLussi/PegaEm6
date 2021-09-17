class Jogador:
    def __init__(self, nome="", mao=[], pontuacao=0):
        self.nome = nome
        self.mao = mao
        self.pontuacao = pontuacao

    def limpar(self):
        self.pontuacao = 0
        self.mao = []