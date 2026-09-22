class Cliente:
    quantidade = 0

    def __init__(self, nome):
        self.nome = nome
        Cliente.quantidade += 1 # sempre que um objeto for criado, vai somar + 1

a = Cliente('Ana') 
b = Cliente('Josefa')

print(Cliente.quantidade)