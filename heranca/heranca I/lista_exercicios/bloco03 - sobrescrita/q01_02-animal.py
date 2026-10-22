class Animal:
    def __init__(self):
        pass

    def emitir_som(self):
        return ("SOM GENÉRICO")


class Cachorro(Animal):
    def __init__(self):
        super().__init__()

    def emitir_som(self):
        return ('AU AU AU AU')

class Gato(Animal):
    def __init__(self):
        super().__init__()

    def emitir_som(self):
        return ('MIAU miau miau')


animalzinho = Animal()

cachorrinho = Cachorro()

gatinho = Gato()

lista_animais: list = [animalzinho, cachorrinho, gatinho]
for i in lista_animais:
    print(i.emitir_som())