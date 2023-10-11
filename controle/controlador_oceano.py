from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano

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
        self.__oceano_computador = self.__oceano_player[:]

    def posiciona_navios(self):
        pass

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