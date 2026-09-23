class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self._nota = 0

    @property
    def nota(self):
        return f'A nota do aluno {self.nome} foi: {self.nota}'

    @nota.setter
    def nota(self, valor):
        if valor <= 0 and valor >=0:
            raise ValueError('Nota inválida. Apenas valores entre 0 e 10!')
        self._nota = valor