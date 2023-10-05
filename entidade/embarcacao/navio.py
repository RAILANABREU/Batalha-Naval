from abc import ABC, abstractmethod

class Navio(ABC):
    @abstractmethod
    def __init__(self, vida, tamanho):
        pass
    
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