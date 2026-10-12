'''
composição
histórico nasce dentro do init de outra classe e morre se ela morrer
    historico depende de conta
    se conta nao existe, historico também não

'''

class Historico:
    def __init__(self) -> None:
        self._operacoes: list[str] = []

    def registrar(self, operacao: str) -> None:
        self._operacoes.append(operacao)

    def __str__(self) -> str:
        for operacao in self._operacoes:
            return operacao

class Conta:
    def __init__(self, titular: str) -> None:
        self._titular = titular
        self._saldo = 0
        self._historico = Historico() # composicao AQUI

    def depositar(self, valor: float) -> None:
        self._saldo += valor
        self._historico.registrar(valor)
        print(f'Depósito de R${valor:.2f}')

    def __str__(self):
        return f'{self._titular}, {self._saldo}'


conta01 = Conta('Chumbrega')
conta01.depositar(70.4)
print(conta01)