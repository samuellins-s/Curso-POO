class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto # agregacao
        self.quantidade = quantidade

    @property
    def subtotal(self) -> float:
        return self.produto * self.quantidade

class Pedido:
    def __init__(self, cliente: "Cliente") -> None:
        self.cliente = cliente
        self._itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        item = ItemPedido(produto, quantidade)
        self._itens.append(item)

    @property
    def total(self) -> float:
        for item in self._itens:
            total_itens = sum(item.subtotal)
        return total_itens

class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._pedidos: list[Pedido] = []

    def fazer_pedido(self, pedido: Pedido) -> None:
        self._pedidos.append(pedido)