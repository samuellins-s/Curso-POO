class ItemAcervo:
    def __init__(self, titulo='', autor='', ano_publicacao=0, vezes_emprestado=0):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.vezes_emprestado = vezes_emprestado

    def emprestar(self):
        self.vezes_emprestado += 1

class Livro(ItemAcervo):
    def __init__(self, titulo='', autor='', ano_publicacao=0, vezes_emprestado=0, num_paginas=0, genero=''):
        super().__init__(titulo, autor, ano_publicacao, vezes_emprestado)
        self.num_paginas = num_paginas
        self.genero = genero

    def resenhar(self):
        return f'O livro {self.titulo} do autor {self.autor} foi resenhado.'

class Revista(ItemAcervo):
    def __init__(self, titulo='', autor='', ano_publicacao=0, vezes_emprestado=0, edicao='', periodicidade=0):
        super().__init__(titulo, autor, ano_publicacao, vezes_emprestado)
        self.edicao = edicao
        self.periodicidade = periodicidade

    def arquivar(self):
        return f'A revista {self.titulo} de edição {self.edicao} foi arquivada.'

class DVD(ItemAcervo):
    def __init__(self, titulo='', autor='', ano_publicacao=0, vezes_emprestado=0, duracao_minutos=0, diretor=''):
        super().__init__(titulo, autor, ano_publicacao, vezes_emprestado)
        self.duracao_minutos = duracao_minutos
        self.diretor = diretor

    def assistir(self):
        return f'O DVD de titulo {self.titulo} com duração de {self.duracao_minutos} foi assistido'

    