class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __str__(self) -> str:
        return self.nome


class Pedido:
    def __init__(self, numero: int, cliente: Cliente, total: float) -> None:
        self.numero = numero
        self.cliente = cliente
        self.total = total

    @property
    def resumo(self) -> str:
        return f'Pedido #{self.numero} | Cliente: {self.cliente} | Total: R$ {self.total:.2f}'


cliente = Cliente("Julia Santos")
pedido = Pedido(101, cliente, 250.00)

print(pedido.resumo)