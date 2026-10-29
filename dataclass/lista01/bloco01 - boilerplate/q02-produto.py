from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int = 0

    def valor_em_estoque(self):
        return self.preco * self.estoque


p1 = Produto('Teclado', 125.90, 5)
p2 = Produto('Mouse', 57.80)

print(p1) # mostra o __repr__
print(p1 == p2) # mostra o __eq__ -> false -> tudo tem que ser igual
print(p1.valor_em_estoque())

