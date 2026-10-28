from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str) -> None:
        self._nome = nome

    @abstractmethod
    def mover_se(self) -> None:
        '''Toda subclasse deve implementar'''

a = Animal('Genérico')

