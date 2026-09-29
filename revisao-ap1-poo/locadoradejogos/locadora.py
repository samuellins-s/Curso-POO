from jogo import Jogo

class ErroDeLocadora(Exception):
    '''Erro!'''
class JogoIndisponivelError(ErroDeLocadora):
    '''O jogo esta indisponivel'''
class JogoNaoEncontradoError(ErroDeLocadora):
    '''O jogo não foi encontrado'''
class JogoDuplicado(ErroDeLocadora):
    '''O jogo está duplicado'''

class Locadora:
    def __init__(self) -> None:
        self.__acervo = []

    def cadastrar(self, jogo: Jogo) -> None:
        for i in self.__acervo:
            if i == jogo:
                raise JogoDuplicado('Este jogo já existe')
        self.__acervo.append(jogo)

    def _buscar(self, nome: str) -> None:
        for i in self.__acervo:
            if i == nome:
                return i
        raise JogoNaoEncontradoError(f'O jogo de título {nome} não foi encontrado')

    def emprestar(self, nome: str) -> None:
        if ...:
            ...
locadora = Locadora()
locadora.cadastrar('Zelda', 'Switch', 2023)