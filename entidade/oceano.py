class Oceano:
    def __init__(self, tamanho_oceano):
        self.__tamanho_oceano = tamanho_oceano
        self.__oceano_player = [[0] * self.__tamanho_oceano for j in range(self.__tamanho_oceano)]
        self.__oceano_computador = [[0] * self.__tamanho_oceano for j in range(self.__tamanho_oceano)]

    @property
    def tamanho_oceano(self):
        return self.__tamanho_oceano
    
    @property
    def oceano_player(self):
        return self.__oceano_player
    
    @property
    def oceano_computador(self):
        return self.__oceano_computador