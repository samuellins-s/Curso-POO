'''
Vamos lá...
criar a classe aluno
    definir init e parametros
    criar metodos
        como criar metodos que acessem variaveis externas?

'''

class Aluno:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def lancar_nota(self, valor: float):
        self.notas.append(valor)

    def media(self) -> float:
        return sum(self.notas) / len(self.notas)

    def aprovado(self) -> bool:
        if self.media() >= 6:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.nome} ({self.matricula}) -- {self.media()}'

aluno1 = Aluno('Joabah', '23904723')
aluno1.lancar_nota(6)

if aluno1.aprovado():
    print(f'{aluno1} aprovado!!!')
