class Pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, salario: float) -> None:
        super().__init__(nome, cpf)
        self.salario = salario


jorginho_atacadao = Funcionario('Jorginho', '11236579519', 2000)
print(jorginho_atacadao.nome) # atributo superclasse
print(jorginho_atacadao.salario)