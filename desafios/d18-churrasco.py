'''
consumo padrão p/pessoa = 480g
preço kg de carne = R$82,40

mostrar quanto de carne deve ser comprado com base na quantidade de pessoas
    carne total = 480 * quantidade pessoas
    custo total do churrasco -> preço da carne total = 82.40 * carne total

    preço para cada pessoa -> custo total/pessoas
    
'''

class Churrasco:
    def __init__(self, pessoas):
        self.quantidade_pessoas = pessoas

    def analisar(self):
        preco_kg_carne = 82.4
        consumo_pessoa = 480

        carne_total = consumo_pessoa * self.quantidade_pessoas
        preco_total = preco_kg_carne * carne_total
        preco_pessoa = preco_total / self.quantidade_pessoas
        
        return f'Preço da carne: {preco_kg_carne}/kg;\nConsumo por pessoa: {consumo_pessoa};\nQuantidade de pessoas: {self.quantidade_pessoas};\nCarne total necessária: {carne_total};\nPreço total da carne: {preco_total:.2f};\nPreço por pessoa: {preco_pessoa:.2f}.'

churrasco1 = Churrasco(6)
print(churrasco1.analisar())