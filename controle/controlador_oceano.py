from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano
from controlador_partida import ControladorPartida
from entidade.embarcacao.submarino import Submarino
from entidade.embarcacao.bote import Bote
from entidade.embarcacao.porta_avioes import PortaAvioes
from entidade.embarcacao.fragata import Fragata
from entidade.partida import Partida


class ControladorOceano:
    def __init__(self, controlador_geral):
        self.__tela_oceano = TelaOceano()
        self.__controlador_geral = controlador_geral

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
        barcos_player = Partida.navios_player()
        barcos_computador = Partida.navios_computador()
        for boat in barcos_player:
            if isinstance(boat, Bote):    
                posicao = self.__tela_oceano.posiciona_navios()
                self.__oceano_player[posicao[0]][posicao[1]] = 'B'

            elif isinstance(boat, Fragata):
                pass