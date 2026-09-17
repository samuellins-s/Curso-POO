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

aluno1 = Aluno('Keliomar da Costina', '23904723')
aluno1.lancar_nota(6)

aluno2 = Aluno('Conscrito Silvandro', '23195792')
aluno2.lancar_nota(3)

aluno3 = Aluno('Namaima do Corvado', '22064773')
aluno3.lancar_nota(9)

if aluno1.aprovado():
    print(f'Aluno(a) {aluno1} aprovado(a)!!!')

if aluno2.aprovado():
    print(f'Aluno(a) {aluno2} aprovado(a)!!!')

if aluno3.aprovado():
    print(f'Aluno(a) {aluno3} aprovado(a)!!!')