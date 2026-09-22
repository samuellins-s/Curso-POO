'''
"Eu quero criar um objeto novo e devolvê-lo?" → provavelmente termina em return cls(...)

"Eu só quero ler ou calcular algo sobre a classe (um total, uma configuração, etc)?" → termina em return cls.algum_atributo (sem parênteses de chamada)

'''

class Produto:
    contador = 0

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        Produto.contador += 1

    @classmethod
    def total_criados(cls):
        return cls.contador

Produto("Caneta", 2.5)
Produto("Caderno", 10.0)
Produto("Lapis", 1.0)

print(Produto.total_criados())  # deve imprimir: 3