class Pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

    def __str__(self) -> str:
        return f'Sou {self.nome}, com cpf {self.cpf}'


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, salario: float) -> None:
        super().__init__(nome, cpf)
        self.salario = salario

    def __str__(self) -> str:
        base = super().__str__()
        return f'{base} e salário {self.salario}'

    def calcular_salario(self) -> float:
        return self.salario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario) -> None:
        super().__init__(nome, cpf, salario)

    def calcular_salario(self, bonus: float) -> float:
        base = super().calcular_salario()
        return base + bonus

func_generico = Funcionario('Aboaba', '85478327480', 1620)
print(func_generico)
print(func_generico.calcular_salario())

func_gerente = Gerente('Jorjão', '48327498237', 1620)
print(func_gerente)
print(func_gerente.calcular_salario(1000))