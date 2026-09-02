class Livro:
    def __init__(self, paginas):
        self.paginas = paginas

    def avancar_paginas(self, quantidade):
        pagina_atual = 1
        if pagina_atual <= quantidade:
            pagina_atual += quantidade
            return f'Página atual: {pagina_atual}'
        else:
            return f'Você terminou o livro'

livro_romance = Livro(30)
print(livro_romance.avancar_paginas(7))
print(livro_romance.avancar_paginas(10))
print(livro_romance.avancar_paginas(30))