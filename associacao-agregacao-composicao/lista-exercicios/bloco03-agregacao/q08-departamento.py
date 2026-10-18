class Professor:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Departamento:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.professores: list[Professor] = []

    def adicionar_professor(self, professor: Professor) -> None:
        self.professores.append(professor)

    def extinguir(self) -> None:
        self.professores.clear()
        print(f'Departamento {self.nome} extinto')


marcos = Professor("Marcos")
helena = Professor("Helena")

comp = Departamento("Computação")
comp.adicionar_professor(marcos)
comp.adicionar_professor(helena)
print(f"Departamento {comp.nome}: {', '.join(p.nome for p in comp.professores)}")

comp.extinguir()
print(f"Marcos ainda existe: {isinstance(marcos, Professor)}")

eng = Departamento("Engenharia")
eng.adicionar_professor(marcos)
print(f"Departamento {eng.nome}: {', '.join(p.nome for p in eng.professores)}")