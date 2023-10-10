from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano

class ControladorOceano:
    def __init__(self, controlador_geral):
        self.__tela_oceano = TelaOceano()
        self.__controlador_geral = controlador_geral

    def montar_oceano(self):
        tamanho_oceano = self.__tela_oceano.tamanho_oceano()
        linha = [0] * tamanho_oceano
        mapa = [linha] * tamanho_oceano
        

    def posiciona_navios(self):
        pass