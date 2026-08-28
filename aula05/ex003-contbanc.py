class ContaBancaria:
    '''
    Documentação class ContaBancaria

    Cria uma conta bancária e permite fazer saques e depósitos
    '''
    def __init__(self, numero, titular, saldo = 0):
        self.numero_da_conta = numero
        self.nome_titular = titular
        self.saldo_conta = saldo
        print(f'Conta {self.numero_da_conta} criada com sucesso. Saldo atual de R${self.saldo_conta:,.2f}.')

    def __str__(self):
        return f'Dados do Titular: nome = {self.nome_titular} ; numero = {self.numero_da_conta} ; saldo = R${self.saldo_conta:,.2f}.'

    def depositar(self, valor):
        self.saldo_conta += valor
        print(f'Depósito de R${valor:,.2f} autorizado com sucesso na conta {self.numero_da_conta}.')

    def sacar(self, valor):
        if valor > self.saldo_conta:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.numero_da_conta}: SALDO INSUFICIENTE')

        else: 
            self.saldo_conta -= valor
            print(f'Saque de R${valor:,.2f} autorizado com sucesso na conta {self.numero_da_conta}.')


conta1 = ContaBancaria(32198432, 'Samuel de Macedo', 2546)

conta1.depositar(789)
conta1.sacar(80051210)

print(conta1)