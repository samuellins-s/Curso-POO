class ContaBancaria:
    '''
    Documentação class ContaBancaria

    Cria uma conta bancária e permite fazer saques e depósitos
    '''
    def __init__(self, numero, titular, saldo = 0):
        self.numero_da_conta = numero # public
        self._nome_titular = titular # protected
        self.__saldo_conta = saldo # private
        print(f'Conta {self.numero_da_conta} criada com sucesso. Saldo atual de R${self.__saldo_conta:,.2f}.')

    def __str__(self):
        # return f'Dados do Titular: nome = {self.nome_titular} ; numero = {self.numero_da_conta} ; saldo = R${self.saldo_conta:,.2f}.'
        return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor) # valor absoluto -> como um módulo -> se negativo, torna positivo
        self.__saldo_conta += valor
        print(f'Depósito de R${valor:,.2f} autorizado com sucesso na conta {self.numero_da_conta}.')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo_conta:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.numero_da_conta}: SALDO INSUFICIENTE')

        else: 
            self.__saldo_conta -= valor
            print(f'Saque de R${valor:,.2f} autorizado com sucesso na conta {self.numero_da_conta}.')