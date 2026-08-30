class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrarEtiqueta(self):
        return f'Etiqueta do produto: nome = {self.nome} ; preço = {self.preco}.'

cocacola = Produto('Cola-Cola', 8.50)
print(cocacola.mostrarEtiqueta())