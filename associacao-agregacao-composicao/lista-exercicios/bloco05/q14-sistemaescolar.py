'''
Escola - Turma: escola possui turmas: composicao
Turma - Aluno: turma possui alunos: agregacao
Turma - Disciplina: turma tem disciplinas: composicao
Professor - Disciplina: professor tem disciplinas: composicao

'''

class Disciplina:
    def __init__(self, nome_disciplina: str) -> None:
        self.nome_disciplina = nome_disciplina


class Aluno:
    def __init__(self, nome_aluno: str) -> None:
        self.nome_aluno = nome_aluno


class Professor:
    def __init__(self, nome_prof: str) -> None:
        self.nome_prof = nome_prof
        self.disciplinas: list[Disciplina] = []


class Turma:
    def __init__(self, nome_turma: str) -> None:
        self.nome_turma = nome_turma
        self.alunos: list[Aluno] = []
        self.disciplinas: list[Disciplina] = []
        self.professores: list[Professor] = []

    def matricular_aluno(self, nome_aluno: str) -> None:
        self.alunos.append(Aluno(nome_aluno))
        print(f'Aluno(a) {nome_aluno} matriculado(a) com SUCESSO!\n')

    def adicionar_disciplina(self, nome_disciplina: str) -> None:
        self.disciplinas.append(Disciplina(nome_disciplina))
        print(f'Disciplina {nome_disciplina} adicionada com SUCESSO!\n')

    def atribuir_professor(self, nome_prof: str) -> None:
        self.professores.append(Professor(nome_prof))
        print(f'Professor(a) {nome_prof} atribuído com SUCESSO na disciplina {self.nome_turma}!')


class Escola:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.turmas: list[Turma] = []

    def criar_turma(self, nome_turma: str) -> None:
        self.turmas.append(Turma(nome_turma))
        print(f'A turma {nome_turma} foi criada com SUCESSO!\n')
    
    def total_alunos(self) -> None:
        pass
