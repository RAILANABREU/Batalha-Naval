from entidade.embarcacao.navio import Navio

class Fragata(Navio):
    def __init__(self, tamanho):
        super().__init__(tamanho)
    
    @property
    def tamanho(self):
        return self.__tamanho