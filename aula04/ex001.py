# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instancia
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

# Declaração de Objetos
g1 = Gafanhoto() # objeto g1
g1.nome = 'Samuel'
g1.idade = 18
print(g1.mensagem())

g2 = Gafanhoto() # objeto g2
g2.nome = 'Maria'
g2.idade = 15
g2.aniversario() # += 1 (16)
print(g2.mensagem())