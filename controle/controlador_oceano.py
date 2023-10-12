from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano
from controlador_partida import ControladorPartida
from entidade.embarcacao.submarino import Submarino
from entidade.embarcacao.bote import Bote
from entidade.embarcacao.porta_avioes import PortaAvioes
from entidade.embarcacao.fragata import Fragata


class ControladorOceano:
    def __init__(self, controlador_geral):
        self.__tela_oceano = TelaOceano()
        self.__controlador_geral = controlador_geral
        self.__oceano_player = None
        self.__oceano_computador = None

    def montar_oceano(self):
        tamanho_oceano = self.__tela_oceano.tamanho_oceano()
        linha = [0] * tamanho_oceano
        mapa = [linha] * tamanho_oceano
        self.__oceano_player = mapa
        self.__oceano_computador = mapa

    def mostrar_oceano(self):
        for linha in range(len(self.__oceano_player)):
            if linha == 0:
                print(f'Y/X   {linha}', end='   ')
            else:
                print(f'{linha}', end='   ')
        print()
        for linha in range(len(self.__oceano_player)):
            for coluna in range(len(self.__oceano_player)):
                if coluna == 0:
                    print(f' {linha}   [{self.__oceano_player[linha][coluna]}]', end=' ')
                else:
                    print(f'[{self.__oceano_player[linha][coluna]}]', end=' ')
            print()
    
    def posiciona_navios(self):
        barcos_player = ControladorPartida.navio_player()
        barcos_computador = ControladorPartida.navio_computador()
        for boat in barcos_player:
            if isinstance(boat, Bote):    
                posicao = self.__tela_oceano.posiciona_navios()
                self.__oceano_player[posicao[0]][posicao[1]] = 'B'

            elif isinstance(boat, Fragata):
                pass