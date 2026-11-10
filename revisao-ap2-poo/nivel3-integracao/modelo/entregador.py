from abc import ABC, abstractmethod

class Entregador(ABC):
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome
        self.limite_distancia = 0

    @abstractmethod
    def taxa_entrega(self, distancia: float) -> float:
        pass


class DeBike(Entregador):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.limite_distancia = 10

    def taxa_entrega(self, distancia):
        VALOR_KM = 0.7 
        return VALOR_KM * distancia


class DeMoto(Entregador):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.limite_distancia = 25

    def taxa_entrega(self, distancia):
        VALOR_KM = 0.5
        return VALOR_KM * distancia