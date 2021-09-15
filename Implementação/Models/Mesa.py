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
    
    # Redefine os jogadores
    def iniciarPartida(self, qtJogadores):
        self.jogadores = [Jogador(f"Jogador {i+1}") for i in range(qtJogadores)]
    
    # Redefine uma partida, limpa os jogadores
    def redefinirPartida(self):
        for jogador in self.jogadores:
            jogador.limpar()

    def obterNovoBaralho(self):
        baralho = []
        for i in range(1, 105): # São 105 cartas
            pontuacao = 1   # Pontuação padrão = 1
        
            if i == 55: # Se carta for múltipla de 55, pontuação = 7
                pontuacao = 7
                baralho.append(Carta(i, pontuacao))
                continue
        
            if i % 5 == 0:  # Se carta for múltipla de 5, pontuação++
                pontuacao += 1
        
            if i % 10 == 0: # Se carta for múltipla de 10, pontuação++
                pontuacao += 1

            if i % 11 == 0: # Se carta for múltipla de 11, pontuação += 4
                pontuacao += 4
            
            baralho.append(Carta(i, pontuacao))

        shuffle(baralho)    # Embaralha o novo baralho criado
        return baralho

    # A partir de um novo baralho, redistribuir as cartas para as fileiras e jogadores
    def redistribuirCartas(self):
        self.lances = []
        self.monte = self.obterNovoBaralho()
        
        for fileira in self.fileiras:   # Distribuir uma carat para cada fileira
            fileira.cartas = [self.monte.pop(0)]
        
        for jogador in self.jogadores:  # Distribui 10 cartas para cada jogador
            jogador.mao = self.monte[:10]
            del self.monte[:10]
        
        # Define jogador atual como o 1º da lista
        self.jogadorAtual = self.jogadores[0]
        
    # Retorna próximo jogador que irá jogar
    def obterProximoJogador(self):
        # Se jogador for o último, retorna o primeiro
        i = (self.jogadores.index(self.jogadorAtual) + 1) % len(self.jogadores)
        return self.jogadores[i]
    
    # Inserção ordenada do lance pelo número da carta
    def incluirLance(self, lance):
        cartaLance = lance.carta.numero
        for i in range(len(self.lances)):
            cartaLanceAtual = self.lances[i].carta.numero
            if cartaLanceAtual > cartaLance:
                self.lances.insert(i, lance)
                return  # Lance inserido
        self.lances.append(lance)   # Lance inserido no final

    # Verifica se jogador atual é último jogador
    def ehUltimoJogador(self):
        return self.jogadorAtual == self.jogadores[-1]
    
    def definirProxJogador(self):
        self.jogadorAtual = self.obterProximoJogador()
    
    # Tenta inserir cada lance nas fileiras
    # Se não for possível inserir um lance, retorna o mesmo
    def avaliarLances(self):
        # Obtém copia do lance para que seja possível remover cada lance ao tratá-lo
        lances = self.lances.copy()
        for lance in lances:    # Tenta inserir um lance
            # Obtém fileiras ordenadas de acordo com as suas maiores cartas
            fileirasOrdenadas = self.obterFileirasOrdenadas()
            for fileira in fileirasOrdenadas:   # Tenta inserir o lance em uma fileira
                if lance.carta.numero > fileira.cartas[-1].numero:
                    # Encontra fileira possível para inserir o lance
                    if len(fileira.cartas) == 5:    # PEGA EM 6
                        for carta in fileira.cartas:    # Atualiza pontuação dos jogadores
                            lance.jogador.pontuacao += carta.pontuacao
                        fileira.limpar()
                    fileira.inserirCarta(lance.carta)
                    self.removerLance(lance)
                    break
                if fileira == fileirasOrdenadas[-1]:
                    # Não foi possível inserir o lance em nenhuma fileira
                    # Jogador do lance precisa escolher uma fileira para substituir
                    return lance

        return None

    def removerLance(self, lance):
        self.lances.remove(lance)
    
    # Retorna fileiras ordenadas de acordo com as suas maiores cartas
    def obterFileirasOrdenadas(self):
        fileirasOrdenadas = [self.fileiras[0]]
        for fileira in self.fileiras[1:]:
            # Insere fileira ordenadamente em fileirasOrdenadas
            maiorCartaFileira = fileira.cartas[-1].numero
            for i in range(len(fileirasOrdenadas)): # Procura por posição adequada
                maiorCartaFileiraOrd = fileirasOrdenadas[i].cartas[-1].numero
                if maiorCartaFileira > maiorCartaFileiraOrd:
                    # Posição adequada encontrada
                    fileirasOrdenadas.insert(i, fileira)
                    break
                elif i+1 == len(fileirasOrdenadas):
                    # Insere no final
                    fileirasOrdenadas.append(fileira)
                    break
        return fileirasOrdenadas
    
    # Retorna lista de jogadores ordenada pelas suas pontuações
    def obterRanking(self):
        jogadores = [self.jogadores[0]]
        for jogadorMesa in self.jogadores[1:]:
            # Insere jogador ordenadamente em jogadores
            for i, jogador in enumerate(jogadores): # Procura por posição adequada
                if jogadorMesa.pontuacao < jogador.pontuacao:
                    # Posição adequada encontrada
                    jogadores.insert(i, jogadorMesa)
                    break
                if i+1 == len(jogadores):
                    # Insere no final
                    jogadores.append(jogadorMesa)
                    break
        return jogadores
    
    # Procura por um jogador com pontuação > 66
    # Se encontrar, é o fim da partida
    def avaliarFimPartida(self):
        for jogador in self.jogadores:
            if jogador.pontuacao > 66:
                return True
        return False