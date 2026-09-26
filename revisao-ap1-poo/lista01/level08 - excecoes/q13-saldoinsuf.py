class SaldoInsuficienteError(Exception):
    '''O saldo é insuficiente!'''

class ContaBancaria:
    def __init__(self, saldo: float, senha: str) -> None:
        self.saldo = saldo
        self.__senha = senha

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError('Digite um saldo positivo!')
        self._saldo = valor

    def sacar(self, valor: float) -> None:
        if valor > self._saldo:
            raise SaldoInsuficienteError('Digite um saque válido!')
        self._saldo -= valor

c = ContaBancaria(100, "1234")
try:
    c.sacar(500)
except SaldoInsuficienteError as e:
    print("Erro:", e)