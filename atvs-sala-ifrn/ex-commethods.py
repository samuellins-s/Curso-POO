class Produto:
    def __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    def total_cadastrados(self,):
        contador += self.quantidade
        return contador

    @classmethod
    def de_csv(cls, nome, valor, quantidade):
        return f'Nome: {nome} ; Valor: {valor} ; Quantidade: {quantidade}.'


televisao = Produto.de_csv('Televisao', 2300, 4)
print(televisao)