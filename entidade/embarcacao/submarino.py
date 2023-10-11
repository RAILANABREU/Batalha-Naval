from entidade.embarcacao.navio import Navio

class Submarino(Navio):
    def __init__(self, vida=2, tamanho=2):
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