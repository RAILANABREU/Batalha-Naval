from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano

class ControladorOceano:
    def __init__(self, controlador_geral):
        self.__tela_oceano = TelaOceano()
        self.__controlador_geral = controlador_geral