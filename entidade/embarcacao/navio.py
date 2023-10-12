from abc import ABC, abstractmethod

class Navio(ABC):
    def __init__(self, vida, tamanho):
        self.__vida = vida
        self.__tamanho = tamanho
    
    @property
    @abstractmethod
    def vida(self):
        pass
    
    @vida.setter
    @abstractmethod
    def vida(self, vida):
        pass

    @property
    @abstractmethod
    def tamanho(self):
        pass