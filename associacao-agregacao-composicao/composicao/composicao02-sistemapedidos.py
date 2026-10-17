class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


class ItemPedido: # tem produto e sua quantidade
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return self.produto * self.quantidade


class Pedido: # pedido tem itens -> valor total dos itens
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente
        self._itens: list[ItemPedido] = []

    def adicionar(self):
        pass

class Cliente: # cliente tem pedidos -> acumula pedidos (append lista)
    pass 

