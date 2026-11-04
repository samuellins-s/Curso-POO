'''
1. 
    Pedido - Cliente: TEM agregação
    Pedido - ItemPedido: TEM composição
    Carrinho - Produto: TEM agregação
    Pessoa - Interruptor: USA associação

2. 



'''

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


class Filho(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)