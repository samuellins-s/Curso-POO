'''
Criar classe Tarefa (título, concluida)
    Montar uma lista com 5 tarefas

Escrever a função concluir(tarefa) que marca concluida = True
    Prove que a mudança aparece na lista

Escrever pendentes(tarefas) que devolve uma nova lista só com as não concluídas

'''

lista_conclusao = []
lista_pendencia = []

class Tarefa:
    def __init__(self):
        self.titulo = ''
        self.conclusao = False

    def concluir(self):
        self.conclusao = True
        lista_conclusao.append(self)
        return lista_conclusao

titulo_tarefas = [
    'arrumar casa', 
    'limpar teclado', 
    'estudar POO', 
    'comer bolacha', 
    'programar'
]

arrumarCasa = Tarefa()
arrumarCasa.titulo = 'Arrumar Casa'
arrumarCasa.conclusao = False
print(arrumarCasa.concluir())