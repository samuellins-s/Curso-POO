from abc import ABC, abstractmethod

'''
Restaurante TEM Cardápio (composicão)
Cardápio TEM Pratos (agregação) - OK

'''

class Prato:
    def __init__(self, nome: str, qtd_pessoas: int) -> None:
        self.nome = nome
        self.qtd_pessoas = qtd_pessoas


class Cardapio:
    def __init__(self) -> None:
        self.pratos: list[Prato] = []

    def adicionar_prato(self, prato: Prato):
        self.pratos.append(prato) # agregacao


class Restaurante:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.cardapio = Cardapio() # composicao


class Entregador(ABC):
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome

    @abstractmethod
    def taxa_entrega(self, distancia: float) -> float:
        pass


class DeBike(Entregador):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def taxa_entrega(self, distancia):
        VALOR_KM = 0.7
        return VALOR_KM * distancia


class DeMoto(Entregador):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def taxa_entrega(self, distancia):
        VALOR_KM = 0.5
        return VALOR_KM * distancia


class Pedido:
    def __init__(self) -> None:
        pass

