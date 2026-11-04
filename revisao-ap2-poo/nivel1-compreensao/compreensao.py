'''
1. 
    Pedido - Cliente: TEM agregação,
    Pedido - ItemPedido: TEM composição,
    Carrinho - Produto: TEM agregação,
    Pessoa - Interruptor: USA associação.

2. 
    Se o super init for esquecido, conforme a demonstração do codigo, consigo acessar mesmo assim, os atributos herdados da superclasse. O super init deixa explicito, nesse caso, os atributos herdados de Pessoa (superclasse).

3.
    Sem executar: a saida de d.ola será a saida de C (olá de C), pois há ordem de prioridade da esquerda para direita.

4. 
    Não sei.

5.
    Um método com pass, diferentemente do metodo abstrato onde ha obrigatoriedade de implementação nas subclasses, torna-se a sua implementação opcional nas subclasses.


'''

# 2
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


class Filho(Pessoa):
    pass

filhinho = Filho('Caba', 7)
print(filhinho.nome)
