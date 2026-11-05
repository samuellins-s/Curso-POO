from entregador import Entregador
from error import EntregaForaDeAreaError

'''
Restaurante TEM Cardápio (composicão)
Cardápio TEM Pratos (agregação) - OK
Pedido TEM Clientes (associação)
Pedido TEM Itens (composição) - OK
Pedido recebe Entregador no init (injeção) - OK

'''

class Prato:
    def __init__(self, nome: str, qtd_pessoas: int, preco: float) -> None:
        self.nome = nome
        self.preco = preco
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


class Item:
    def __init__(self, prato: Prato, quantidade: int) -> None:
        self.prato = prato
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return self.prato.preco * self.quantidade


class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Pedido:
    def __init__(self, entregador: Entregador) -> None:
        self.entregador = entregador # injecao
        self.itens: list[Item] = []
    
    def total(self, distancia: float) -> float:
        if distancia > self.entregador.limite_distancia:
            raise EntregaForaDeAreaError(f'O entregador {self.entregador.nome} não consegue entregar, o seu limite de entrega é no raio de {self.entregador.limite_distancia} KM')
        subtotais = sum(item.subtotal() for item in self.itens)
        return subtotais + self.entregador.taxa_entrega(distancia)
