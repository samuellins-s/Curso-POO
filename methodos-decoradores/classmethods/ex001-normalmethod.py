class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudar(self): # metodo self. só existe quando um objeto já é criado
        print(f'Olá! Eu me chamo {self.nome} e tenho {self.idade} anos!')

p1 = Pessoa('Luiziana', 60)
p1.saudar()