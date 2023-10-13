from entidade.oceano import Oceano
from entidade.embarcacao.bote import Bote
from entidade.embarcacao.fragata import Fragata
from entidade.embarcacao.porta_avioes import PortaAvioes
from entidade.embarcacao.submarino import Submarino
from entidade.jogador import Jogador

class Partida:
    def __init__(self, jogador, tamanho_oceano):
        self.__bote1_player = Bote(vida=1, tamanho=1)
        self.__bote2_player = Bote(vida=1, tamanho=1)
        self.__bote3_player = Bote(vida=1, tamanho=1)
        self.__fragata1_player = Fragata(vida=3, tamanho=3)
        self.__fragata2_player = Fragata(vida=3, tamanho=3)
        self.__porta_avioes_player = PortaAvioes(vida=4, tamanho=4)
        self.__submarino1_player = Submarino(vida=2, tamanho=2)
        self.__submarino2_player = Submarino(vida=2, tamanho=2)

        self.__bote1_computador = Bote(vida=1, tamanho=1)
        self.__bote2_computador = Bote(vida=1, tamanho=1)
        self.__bote3_computador = Bote(vida=1, tamanho=1)
        self.__fragata1_computador = Fragata(vida=3, tamanho=3)
        self.__fragata2_computador = Fragata(vida=3, tamanho=3)
        self.__porta_avioes_computador = PortaAvioes(vida=4, tamanho=4)
        self.__submarino1_computador = Submarino(vida=2, tamanho=2)
        self.__submarino2_computador = Submarino(vida=2, tamanho=2)

        self.__navios_player = [self.__bote1_player, self.__bote2_player,
                                self.__bote3_player, self.__fragata1_player,
                                self.__fragata2_player, self.__porta_avioes_player,
                                self.__submarino1_player, self.__submarino2_player]
        
        self.__navios_computador = [self.__bote1_computador, self.__bote2_computador,
                                    self.__bote3_computador, self.__fragata1_computador,
                                    self.__fragata2_computador, self.__porta_avioes_computador,
                                    self.__submarino1_computador, self.__submarino2_computador] 
        
        self.__oceano_player = Oceano(tamanho_oceano)
        self.__oceano_computador = Oceano(tamanho_oceano)

        self.__jogador = jogador


    @property
    def jogador(self):
        return self.__jogador

    @property
    def navios_player(self):
        return self.__navios_player
    
    @property
    def navios_computador(self):
        return self.__navios_computador
    
    @property
    def oceano_player(self):
        return self.__oceano_player
    
    @property
    def oceano_computador(self):
        return self.__oceano_computador