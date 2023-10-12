from limite.tela_partida import TelaPartida
from entidade.partida import Partida

class ControladorPartida:
    def __init__(self, controlador_geral):
        self.__lista_partidas = []
        self.__tela_partida = TelaPartida()
        self.__navio_player = []
        self.__navio_computador = []
        self.__controlador_geral = controlador_geral

    def navio_player(self):
        return self.__navio_player

    def navio_computador(self):
        return self.__navio_computador

    def pontuacao(self):
        pass