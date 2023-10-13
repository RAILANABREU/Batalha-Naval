class Pontuacao:
    def __init__(self, pontuacao_total=0):
        self.__pontuacao_total = pontuacao_total

    @property
    def pontuacao_total(self):
        return self.__pontuacao_total
    
    @pontuacao_total.setter
    def pontuacao_total(self, pontuacao_total):
        self.__pontuacao_total = pontuacao_total + 1