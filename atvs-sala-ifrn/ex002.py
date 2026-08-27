'''
Considere a abstração de um objeto carro. Crie uma classe que
possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.

'''

class Carro:
    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.ano = None

    def mensagem(self):
        return f'Configurações do carro desejado:\nMarca: {self.marca}. Modelo: {self.modelo}. Ano: {self.ano}.'

# carro 1
carro1 = Carro() # objeto
print(carro1.mensagem())

carro2 = Carro()
carro2.marca = 'Volksvagem'
carro2.modelo = 'Top'
carro2.ano = 2010
print(carro2.mensagem())