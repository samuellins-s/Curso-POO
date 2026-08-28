# Declaração de Classe
class Gafanhoto:
    '''
    Documentação da class Gafanhoto

    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    '''
    def __init__(self, nome = '', idade = 0): # Método Construtor
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # str dunder method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}.'
# Declaração de Objetos
g1 = Gafanhoto('Samuel', 18) # objeto g1

print(g1.__doc__) # None -> não existe documentação. Com docstring, há documentação
print(g1) # com dunder method __str__ já retorna automaticamente

print(g1.__dict__) # atributo dict -> retorna forma dicionário
print(g1.__getstate__()) # forma dicionario, mas personalizavel
print(g1.__class__) # saber qual a classe do objeto