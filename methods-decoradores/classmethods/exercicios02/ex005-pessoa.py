class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def a_partir_de_string(cls, texto):
        nome, idade = texto.split(',')
        return cls(nome, int(idade))

    def __str__(self):
        return f'Nome: {self.nome} ; Idade: {self.idade}'

    def __repr__(self):
        return self.__str__() # reaproveita o str

p1 = Pessoa('Samuel', 18)
p2 = Pessoa.a_partir_de_string('Samuel,18')
print(p2)