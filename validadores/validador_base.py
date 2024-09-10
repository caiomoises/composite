from abc import ABC, abstractmethod

class validador(ABC):
    @abstractmethod
    def validar(self, valor):
        pass