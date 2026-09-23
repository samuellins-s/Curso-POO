class Livro:
    contador = 0

    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        Livro.contador += 1

    @classmethod
    def quantidade_de_livros(cls):
        return cls.contador

Livro("Dom Casmurro", "Machado de Assis")
Livro("O Cortiço", "Aluísio Azevedo")

print(Livro.quantidade_de_livros())  # 2