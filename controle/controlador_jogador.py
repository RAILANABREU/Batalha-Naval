from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador

class ControladorJogador:
    def __init__(self, controlador_geral):
        self.__lista_jogadores = []
        self.__historico_partidas = []
        self.__tela_jogador = TelaJogador()
        self.__controlador_geral = controlador_geral

    def pega_jogador_por_id(self, id):
        for jogador in self.__lista_jogadores:
            if(jogador.id == id):
                return jogador
        return None

    def inserir_jogador(self):
        dados_jogador = self.__tela_jogador.dados_jogador()
        player = Jogador(dados_jogador["nome"], dados_jogador["data_nascimento"], dados_jogador["id"])
        self.__lista_jogadores.append(player)

    def alterar_jogador(self):
        self.listar_jogadores()
        id_jogador = self.__tela_jogador.seleciona_jogador()

    def listar_jogadores(self):
        for jogador in self.__lista_jogadores:
            self.__tela_jogador.mostra_jogador({"nome": jogador.nome, "data_nascimento": jogador.data_nascimento, "id": jogador.id})

    def historico_partidas(self):
        pass

    def deletar_jogador(self):
        self.listar_jogadores()
        id_jogador = self.__tela_jogador.seleciona_jogador() 
        jogador = self.pega_jogador_por_id(id_jogador)
        if jogador is not None:
            self.__lista_jogadores.remove(jogador)

    def retornar(self):
        self.__controlador_geral.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.inserir_jogador, 2: self.alterar_jogador, 3: self.listar_jogadores, 4: self.historico_partidas, 5: self.rank, 6: self.deletar_jogador, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()