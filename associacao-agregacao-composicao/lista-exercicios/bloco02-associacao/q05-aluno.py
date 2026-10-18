class Aluno:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.cursos: list[Curso] = []



class Curso:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.alunos: list[Aluno] = []

    def matricular(self, aluno: Aluno) -> None:
        self.alunos.append(aluno)
        aluno.cursos.append(self)


lucas = Aluno("Lucas")
carla = Aluno("Carla")
python = Curso("Python")
redes = Curso("Redes")

python.matricular(lucas)
python.matricular(carla)
redes.matricular(lucas)

print(f"Cursos de {lucas.nome}: {', '.join(c.nome for c in lucas.cursos)}")
print(f"Alunos de {python.nome}: {', '.join(a.nome for a in python.alunos)}")
print(f"Alunos de {redes.nome}: {', '.join(a.nome for a in redes.alunos)}")