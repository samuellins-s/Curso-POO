class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def cumprimentar(self) -> str:
        print(f'{self.nome} cumprimentando!')


class Aluno(Pessoa):
    def estudar(self) -> str:
        print(f'Aluno {self.nome} está estudando...')


class Professor(Pessoa):
    def lecionar(self) -> str:
        print(f'Professor {self.nome} está lecionando...')


jorginho = Aluno('Jorginho', 16)
josoares = Professor('Josoares', 48)

jorginho.cumprimentar()
jorginho.estudar()
print()
josoares.cumprimentar()
josoares.lecionar()