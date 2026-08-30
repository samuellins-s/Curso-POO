class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def seApresentar(self):
        return f'Olá! Eu sou Funcionário. Me chamo {self.nome}, sou do setor {self.setor} e o meu cargo é {self.cargo}.'

funcionario1 = Funcionario('Gabriel', 4, 'Analista de Sistemas')
print(funcionario1.seApresentar())
