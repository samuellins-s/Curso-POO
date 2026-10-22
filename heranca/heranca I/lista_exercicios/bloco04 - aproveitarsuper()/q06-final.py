class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def se_apresentar(self) -> str:
        return f'Olá! Sou {self.nome}'


class Aluno(Pessoa):
    def __init__(self, nome, turma: str) -> None:
        super().__init__(nome)
        self.turma = turma

    def se_apresentar(self) -> str:
        base = super().se_apresentar()
        return f'{base}, sou da turma {self.turma}.'


class Professor(Pessoa):
    def __init__(self, nome, nivel: str) -> None:
        super().__init__(nome)
        self.nivel = nivel

    def se_apresentar(self) -> str:
        base = super().se_apresentar()
        return f'{base}, sou {self.nivel}.'


bebe = Pessoa('Bebezinho')
jorginho = Aluno('Jorginho', '2AM')
clovis = Aluno('Clovis', '3BM')
melissaw = Aluno('Melissaw', '3BM')
fabio = Professor('Fábio', 'Mestre')
procopio = Professor('Procópio', 'Doutor')

galera: list[Pessoa] = [jorginho, clovis, melissaw, fabio, procopio, bebe]
for pessoa in galera:
    print(pessoa.se_apresentar())