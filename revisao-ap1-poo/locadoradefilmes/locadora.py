from filme import Filme

class ErroDeLocadora(Exception):
    '''Erro de locadora'''

class FilmeIndisponivelError(ErroDeLocadora):
    '''O filme está indisponível'''

class FilmeNaoEncontradoError(ErroDeLocadora):
    '''O filme não foi encontrado'''

class Locadora:
    def __init__(self) -> None:
        self._catalogo: list[Filme] = []
            
    def cadastrar(self, filme: Filme) -> None:
        self._catalogo.append(filme)

    def _buscar(self, titulo: str) -> Filme:
        for filme in self._catalogo:
            if filme.titulo == titulo:
                return filme
        raise FilmeNaoEncontradoError(titulo)

    def alugar(self, titulo: str) -> None:
        filme = self._buscar(titulo)
        if not filme.disponibilidade_locacao:    
            raise FilmeIndisponivelError(titulo)
        filme.disponibilidade_locacao = False

    def devolver(self, titulo: str) -> None:
        filme = self._buscar(titulo)
        filme.disponibilidade_locacao = True

    def filmes_disponiveis(self) -> None:
        for filme in self._catalogo:
            if filme.disponibilidade_locacao:
                print(filme)


locadora1 = Locadora()
locadora1.cadastrar(Filme('De volta para o futuro', 1978))
