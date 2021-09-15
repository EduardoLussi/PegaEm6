class Fileira:
    def __init__(self, cartas=[]):
        self.cartas = cartas
    
    def limpar(self):
        self.cartas.clear()
    
    def inserirCarta(self, carta):
        self.cartas.append(carta)