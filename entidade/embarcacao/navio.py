from abc import ABC, abstractmethod

class Navio(ABC):
    def __init__(self, tamanho):
        self.__tamanho = tamanho

    @property
    @abstractmethod
    def tamanho(self):
        pass