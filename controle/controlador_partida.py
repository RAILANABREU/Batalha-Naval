from limite.tela_partida import TelaPartida
from entidade.partida import Partida
from entidade.embarcacao.submarino import Submarino
from entidade.embarcacao.bote import Bote
from entidade.embarcacao.porta_avioes import PortaAvioes
from entidade.embarcacao.fragata import Fragata

class ControladorPartida:
    def __init__(self, controlador_geral):
        self.__lista_partidas = []
        self.__tela_partida = TelaPartida()
        self.__navio_player = []
        self.__navio_computador = []
        self.__controlador_geral = controlador_geral

    def distribui_navios(self):
        for i in range(3):
            bote = Bote(tamanho=1, vida=1)
            self.__navio_player.append(bote)
        
        for i in range(2):
            fragata = Fragata(tamanho=3, vida=3)
            self.__navio_player.append(fragata)    

        for i in range(2):
            submarino = Submarino(tamanho=2, vida=2)
            self.__navio_player.append(submarino)

        porta_avioes = PortaAvioes(tamanho=4, vida=4)
        self.__navio_player.append(porta_avioes)
        self.__navio_computador = self.__navio_player[:]

    def navio_player(self):
        return self.__navio_player

    def navio_computador(self):
        return self.__navio_computador

    def pontuacao(self):
        pass