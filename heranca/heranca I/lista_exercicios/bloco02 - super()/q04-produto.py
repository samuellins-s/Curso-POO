class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


class Livro(Produto):
    def __init__(self, nome, preco, autor: str, paginas: int) -> None:
        super().__init__(nome, preco)
        self.autor = autor
        self.paginas = paginas


livrozinho = Livro('Livro do Jorginho', 48.90, 'Jorginho Trumpet', 90)
print(livrozinho.nome) # super
print(livrozinho.preco) # super
print(livrozinho.autor)
print(livrozinho.paginas)
