class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Cachorro(Animal):
    def __init__(self, nome: str, raca: str) -> None:
        super().__init__(nome)
        self.raca = raca


dog = Cachorro('Dogzin', 'Bulldog')
print(dog.nome)
