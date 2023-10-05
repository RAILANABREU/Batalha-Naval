from limite.tela_partida import TelaPartida
from entidade.partida import Partida

class ControladorPartida:
    def __init__(self, controlador_geral):
        self.__lista_partidas = []
        self.__tela_partida = TelaPartida()
        self.__navio_player = []
        self.__navio_computador = []
        self.__controlador_geral = controlador_geral

    def oceano_player(self):
        pass

    def oceano_computador(self):
        pass

    def navio_player(self):
        pass

    def navio_computador(self):
        pass

    def pontuacao(self):
        pass