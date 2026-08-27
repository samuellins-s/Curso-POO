'''
Considere a abstração de um objeto cachorro. Crie uma classe
que possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.

'''

class Cachorro:
    def __init__(self):
        self.raca = ''
        self.cor = ''
        self.idade = None

    def dizerRaca(self):
        return f'Raça: {self.raca}.'

    def dizerCor(self):
        return f'Cor: {self.cor}.'

    def dizerIdade(self):
        return f'Idade: {self.idade}.'

cachorro1 = Cachorro()
cachorro1.raca = 'Lhasa Apso'
cachorro1.cor = 'Branco e Beje'
cachorro1.idade = 6
print(cachorro1.dizerRaca())
print(cachorro1.dizerCor())
print(cachorro1.dizerIdade())