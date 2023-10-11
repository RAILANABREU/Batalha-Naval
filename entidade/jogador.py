from entidade.pontuacao import Pontuacao

class Jogador:
    def __init__(self, nome, data_nascimento, id, pontuacao=Pontuacao):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__id = id
        self.__pontuacao = pontuacao

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id