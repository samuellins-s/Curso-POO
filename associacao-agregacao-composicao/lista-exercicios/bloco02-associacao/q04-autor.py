class Autor:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.livros: list[Livro] = []


class Livro:
    def __init__(self, titulo: str, autor: Autor) -> None:
        self.titulo = titulo
        self.autor = autor
        autor.livros.append(self)


autor = Autor("Machado de Assis")
livro1 = Livro("Dom Casmurro", autor)
livro2 = Livro("Memórias Póstumas", autor)

print(f"Autor: {autor.nome}")
print(f"Livros: {', '.join(l.titulo for l in autor.livros)}")
print(f'Autor de "{livro1.titulo}": {livro1.autor.nome}')