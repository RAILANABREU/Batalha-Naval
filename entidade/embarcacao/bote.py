from entidade.embarcacao.navio import Navio

class Bote(Navio):
    def __init__(self, vida, tamanho):
        super().__init__(vida, tamanho)
        
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida - 1
    
    @property
    def tamanho(self):
        return self.__tamanho