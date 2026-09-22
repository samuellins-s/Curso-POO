class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # protected

    # metodos acessores
    def get_nota(self): # metodo getter
        return self._nota

    def set_nota(self, valor): # metodo setter
        if valor >= 0 and valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida!')

    