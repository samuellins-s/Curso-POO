class Animal:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> str:
        print(f'========== Animal ==========\nNome: {self.nome}\nIdade: {self.idade}')


class Cachorro(Animal):
    pass


dog = Cachorro('Bulacha', 3)
dog.apresentar()