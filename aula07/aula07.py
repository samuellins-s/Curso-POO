class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        return f'{self.nome} acabou de fazer matrícula!'


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        return f'Prof. {self.nome} começou a dar aula!'


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        return f'{self.nome} acabou de bater ponto!'



a1 = Aluno('Arthur Jônatan', 18, 'Redes de Computadores', '2026.2')
a1.fazer_aniversario() # veio da superclasse
a1.fazer_matricula()

p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario('Joberta', 42, 'Secretaria', 'Setor 02')
f1.bater_ponto()