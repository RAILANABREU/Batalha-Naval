from limite.tela_partida import TelaPartida
from entidade.partida import Partida
from entidade.jogador import Jogador

class ControladorPartida:
    def __init__(self, controlador_geral):
        self.__jogador = Jogador("a", "b", 1)
        self.__partida = Partida(self.__jogador, 1)
        self.__tela_partida = TelaPartida()
        self.__controlador_geral = controlador_geral

    def comecar_partida(self):
        info = self.__tela_partida.comecar_partida()
        self.__jogador = self.__controlador_geral.controlador_jogador().pega_jogador_por_id(info["id"])
        tamanho_oceano = int(info["tamanho_oceano"])
        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
            self.__partida = Partida(self.__jogador, tamanho_oceano)
            self.__controlador_geral.controlador_oceano().posiciona_navios(self.__partida.navios_player(), self.__partida.navios_computador())
            self.__controlador_geral.cadastra_oceano()

    def partida(self):
        return self.__partida

    def navio_player(self):
        return self.__partida.navios_player()

    def navio_computador(self):
        return self.__partida.navios_computador()

    def pontuacao(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.comecar_partida, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_partida.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela_partida.mostra_mensagem("Valor inválido, digite um número Válido")