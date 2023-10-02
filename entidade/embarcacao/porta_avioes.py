


class PortaAvioes:
    def __init__(self, vida, tamanho):
        self.__vida = vida
        self.__tamanho = tamanho
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho