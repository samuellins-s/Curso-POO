class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._posicao = 0

    def mover_se(self) -> None:
        print(f'Animal {self.nome} se mexendo...')


class Gato(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def mover_se(self) -> None:
        print(f'Gato {self.nome} caminhando...')


class Peixe(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def mover_se(self) -> None:
        print(f'Peixe {self.nome} nadando...')


class Passaro(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def mover_se(self) -> None:
        print(f'Pássaro {self.nome} voando...')


class Cobra(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def mover_se(self):
        print(f'Cobra {self.nome} rastejando...')


gatinho = Gato('Tom')
peixinho = Peixe('Nemo')
passarinho = Passaro('Pidgey')
animal = Animal('Animal')
cobrinha = Cobra('Snaking')

def mover_todos(animais: list[Animal]):
    for animal in animais:
        animal.mover_se() # polimorfismo


mover_todos([gatinho, peixinho, passarinho, animal, cobrinha])