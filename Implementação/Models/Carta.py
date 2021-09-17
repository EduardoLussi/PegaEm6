class Carta:
    def __init__(self, numero=0, pontuacao=0):
        self.numero = numero
        self.pontuacao = pontuacao
    
    def getPontuacao(self):
        return self.pontuacao
    
    def getNumero(self):
        return self.numero