class Livro:
    def __init__(self, titulo: str, autor: str, preco: float, peso_kg: float) -> None:

        if preco < 0:
            raise ValueError('Insira um preço maior que 0')

        if peso_kg < 0:
            raise ValueError('Insira um peso (kg) maior que 0')

        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.peso_kg = peso_kg

    def __str__(self) -> str:
        return f'Livro: {self.titulo} ; Autor: {self.autor} ; Preço: R$ {self.preco:.2f} ; Peso: {self.peso_kg} kg'
        

class Catalogo:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.livros: list[Livro] = []

    def adicionar(self, livro: Livro) -> None:
        self.livros.append(livro)

    def buscar_por_titulo(self, titulo: str) -> Livro | None:
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def listar(self) -> None:
        print('\nListagem de livros do Catálogo: ')
        for livro in self.livros:
            print(livro)


class Livraria:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.catalogo: Catalogo

    def criar_catalogo(self, nome: str):
        self.catalogo = Catalogo(nome)


livrinhoA = Livro('A', 'Koal', 30, 0.4)
livrinhoB = Livro('B', 'Hoam', 92, 1)

catalogo = Catalogo()
catalogo.adicionar(livrinhoA)
catalogo.adicionar(livrinhoB)
catalogo.listar()
print(catalogo.buscar_por_titulo('A'))