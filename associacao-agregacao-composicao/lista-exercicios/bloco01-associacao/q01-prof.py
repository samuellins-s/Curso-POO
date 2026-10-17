class Disciplina:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __str__(self):
        return self.nome

class Professor:
    def __init__(self, nome: str):
        self.nome = nome

    def ministrar_aula(self, disciplina: Disciplina) -> str:
        return f'Prof. {self.nome} está ministrando {disciplina}'


disc1 = Disciplina("Estruturas de Dados")
disc2 = Disciplina("Banco de Dados")
prof = Professor("Marcos")
print(prof.ministrar_aula(disc1))
print(prof.ministrar_aula(disc2))