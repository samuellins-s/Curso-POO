class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def produto_descricao(self) -> str:
        return f'Produto: {self.nome} | Preço: R$ {self.preco:.2f}'


class Livro(Produto):
    def __init__(self, nome, preco, autor: str, paginas: int) -> None:
        super().__init__(nome, preco)
        self.autor = autor
        self.paginas = paginas


class Eletronico(Produto):
    def __init__(self, nome, preco, garantia_meses: int) -> None:
        super().__init__(nome, preco)
        self.garantia_meses = garantia_meses

    def produto_descricao(self):
        base = super().produto_descricao()
        return f'{base}\nGarantia: {self.garantia_meses} meses'


eletronico = Eletronico('Geladeira', 2356.90, 12)
print(eletronico.produto_descricao())
