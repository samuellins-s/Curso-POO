# QUESTÃO 01

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

# QUESTÃO 02

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f'Área do retangulo: {self.base * self.altura}'

    def perimetro(self):
        return f'Perímetro do retangulo: {(2 * self.base) + (2 * self.altura)}'

    def __eq__(self, other):
        if not isinstance(other, Retangulo):
            return NotImplemented
        return self.base == other.base and self.altura == other.altura

# QUESTÃO 03

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_texto(cls, texto):
        dia, mes, ano = texto.split('/')
        return cls(int(dia), int(mes), int(ano))

    @staticmethod
    def bissexto(ano):
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def __str__(self):
        return f'{self.dia:02d}/{self.mes:02d}/{self.ano:04d}'