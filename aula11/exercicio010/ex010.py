class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # protected

    # criando atributo validavel
    @property
    def nota(self): # getter
        return self._nota

    @nota.setter
    def nota(self, valor): # setter
        if valor >= 0 and valor <= 10:
            self._nota = valor
        else:
            print('Nota INVÁLIDA!!! ')