from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador

class ControladorJogador:
    def __init__(self, controlador_geral):
        self.__lista_jogadores = []
        self.__historico_partidas = []
        self.__tela_jogador = TelaJogador()
        self.__controlador_geral = controlador_geral

    def inserir_jogador(self):
        dados_jogador = self.__tela_jogador
        player = Jogador(dados_jogador["nome"], dados_jogador["data_nascimento"], dados_jogador["id"])
        self.__lista_jogadores.append(player)

    def alterar_jogador(self):
        self.listar_jogadores()
        id_jogador = self.__tela_jogador.seleciona_amigo()

    def listar_jogadores(self):
        pass

    def informacoes_jogador(self):
        pass

    def historico_partidas(self):
        pass

    def deletar_jogador(self):
        pass
