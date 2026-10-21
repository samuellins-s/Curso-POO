class Animal:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> str:
        print(f'========== Animal ==========\nNome: {self.nome}\nIdade: {self.idade}')


class Cachorro(Animal):
    def latir(self) -> str:
        print('AU! AU!! AU!!! AU!!!')


class Gato(Animal):
    def miar(self) -> str:
        print('miau miau miau')


dog = Cachorro('chumbrega', 5)
gatin = Gato('Jaboba', 1)

dog.apresentar()
dog.latir()

gatin.apresentar()
gatin.miar()

print(isinstance(gatin, Gato))
print(isinstance(gatin, Animal))
print(isinstance(gatin, Cachorro))
print(isinstance(dog, Animal))
