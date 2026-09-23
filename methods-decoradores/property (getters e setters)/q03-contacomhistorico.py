class ContaBancaria:

    def __init__(self):
        self._saldo = 0
        self.lista_historico = []

    def depositar(self, valor):
        if valor < 0:
            raise ValueError('Valor menor que 0 (zero)!')
        
        self._saldo += valor
        self.lista_historico.append(f'Depósito: R${valor}')

    def sacar(self, valor):
        if valor > self._saldo:
            raise ValueError('Valor excede o saldo disponível!')
        if valor < 0:
            raise ValueError('Valor menor que 0 (zero)!')

        self._saldo -= valor
        self.lista_historico.append(f'Saque: R${valor}')
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        raise AttributeError('Atributo saldo não pode ser acessado!')

    @property
    def extrato(self):
        return self.lista_historico

conta = ContaBancaria()
conta.depositar(100)
conta.sacar(30)
print(conta.saldo)     # 70
print(conta.lista_historico)   # ['Depósito: R$100', 'Saque: R$30']
conta.saldo = 999      # AttributeError!