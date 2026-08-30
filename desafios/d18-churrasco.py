'''
consumo padrão p/pessoa = 480g
preço kg de carne = R$82,40

mostrar quanto de carne deve ser comprado com base na quantidade de pessoas
    custo total do churrasco
    preço para cada pessoa -> total/pessoas

'''

class Churrasco:
    def __init__(self, pessoas):
        self.quantidade_pessoas = pessoas

    def analisar(self):
        carne_total = 480 * self.quantidade_pessoas

        return f'Consumo de carne por pessoa: 480g\nPreço da carne: R$82,40'
