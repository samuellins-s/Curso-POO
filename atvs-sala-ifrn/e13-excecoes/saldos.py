class SaldoInsuficienteError(Exception):
    '''
    Saque maior que o saldo disponível!
    '''

class ValorInvalidoError(Exception):
    '''
    Valor menor que zero!
    '''

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    def sacar(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteError(f'Saldo atual: {self._saldo} ; Pedido de saque: {valor}')

        if valor < 0:
            raise ValorInvalidoError(f'Saldo atual: {self._saldo} ; Pedido de saque: {valor}')

        self._saldo -= valor

    def depositar(self, valor):
        if valor < 0:
            raise ValorInvalidoError(f'Saldo atual: {self._saldo} ; Pedido de depósito: {valor}')

        self._saldo += valor