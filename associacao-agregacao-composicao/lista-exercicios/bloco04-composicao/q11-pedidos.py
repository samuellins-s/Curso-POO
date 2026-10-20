class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.itens: list[ItemPedido] = []

    def adicionar_item(self, produto: Produto, quantidade: int) -> None:
        itempedido = ItemPedido(produto, quantidade)
        self.itens.append(itempedido)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.itens)

    def imprimir(self) -> None:
        print(f'Pedido #{self.numero}')
        for item in self.itens:
            print(f'{item.quantidade}x {item.produto.nome} --- R$ {item.subtotal:.2f}')
        print(f'Total: R${self.total}')


mouse = Produto("Mouse", 50.00)
teclado = Produto("Teclado", 150.00)

pedido = Pedido(1)
pedido.adicionar_item(mouse, 2)
pedido.adicionar_item(teclado, 1)
pedido.imprimir()