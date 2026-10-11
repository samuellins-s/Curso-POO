'''
1. produto individual
    __str__

2. carrinho de compras
    cria uma lista de produtos no init
    metodo adicionar produto no carro de compras

'''

class Produto:
    def __init__(self, nome: str, valor: float) -> None:
        self.nome = nome
        self.valor = valor

    def __str__(self) -> str:
        return f'{self.nome}: R${self.valor:.2f}'

class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.itens: list[Produto] = [] # agregacao -> criacao de lista de objetos da classe Produto

    def adicionar(self, produto: Produto) -> None:
        self.itens.append(produto)


coquinha = Produto('Coca-Cola Espumante', 8.99)
print(coquinha)
carrinho = CarrinhoDeCompras()
carrinho.adicionar(coquinha)