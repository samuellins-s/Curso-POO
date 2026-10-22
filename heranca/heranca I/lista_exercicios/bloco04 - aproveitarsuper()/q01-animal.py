class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def apresentar(self) -> str:
        return f'Sou o {self.nome}'


class Cachorro(Animal):
    def __init__(self, nome: str, raca: str) -> None:
        super().__init__(nome)
        self.raca = raca

    def apresentar(self) -> str:
        base = super().apresentar()
        return f'{base} da raça {self.raca}'