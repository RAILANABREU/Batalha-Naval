from entidade.embarcacao.navio import Navio

class Bote(Navio):
    def __init__(self, vida=1, tamanho=1):
        self.__vida = vida
        self.__tamanho = tamanho

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida - 1
    
    @property
    def tamanho(self):
        return self.__tamanho