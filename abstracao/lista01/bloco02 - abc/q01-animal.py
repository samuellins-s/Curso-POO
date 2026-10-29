from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def mover_se(self):
        print(f'{self.nome} se movendo...')


class Gato(Animal):
    def mover_se(self):
        print(f'{self.nome} caminhando...')


class Peixe(Animal):
    def mover_se(self):
        print(f'{self.nome} nadando...')


class Passaro(Animal):
    def mover_se(self):
        print(f'{self.nome} voando...')


gatinho = Gato('Tom')
peixinho = Peixe('Neminho')
passarinho = Passaro('Pidgey')

animais = [gatinho, peixinho, passarinho]

def mover_todos(animais: list[Animal]):
    for animal in animais:
        animal.mover_se()

mover_todos(animais)