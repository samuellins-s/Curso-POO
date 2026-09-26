class SalarioInvalidoError(Exception):
    '''Valor menor que zero!'''

class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, valor: float) -> float:
        if valor < 0:
            raise SalarioInvalidoError('Digite um número positivo!')
        self._salario = valor

    def __str__(self) -> str:
        return f'Funcionário: {self.nome} ; Salário: {self.salario}'

    def __repr__(self) -> str:
        return f'Funcionario(nome={self.nome!r}, salario={self.salario})'

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Funcionario):
            return NotImplemented
        return self.salario == outro.salario

    def __lt__(self, outro) -> bool:
        return self.salario < outro.salario

    @classmethod
    def estagiario(cls, nome: str):
        salario_estagio = 820
        return cls(nome, salario_estagio)

f1 = Funcionario("Ana", 3000)
f2 = Funcionario.estagiario("Bruno")

print(f1)                     # __str__
print(repr(f1))               # __repr__
print(f1 == f2)               # __eq__
print(sorted([f1, f2]))       # usa __lt__

try:
    f1.salario = -100
except SalarioInvalidoError as e:
    print("Erro:", e)          # try/except em quem usa a classe