from limite.tela_partida import TelaPartida
from entidade.partida import Partida
from entidade.jogador import Jogador

class ControladorPartida:
    def __init__(self, controlador_geral):
        self.__jogador = Jogador
        self.__partida = Partida
        self.__tela_partida = TelaPartida()
        self.__navio_player = []
        self.__navio_computador = []
        self.__controlador_geral = controlador_geral

    def comecar_partida(self):
        info = self.__tela_partida.comecar_partida()
        self.__jogador = self.__controlador_geral.controlador_jogador().pega_jogador_por_id(info["id"])
        tamanho_oceano = int(info["tamanho_oceano"])
        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
            self.__partida = Partida(self.__jogador, tamanho_oceano)
            self.__controlador_geral.controlador_oceano().posiciona_navios()

    def navio_player(self):
        return self.__navio_player

    def navio_computador(self):
        return self.__navio_computador

    def pontuacao(self):
        pass