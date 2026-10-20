class Transacao:
    def __init__(self, tipo_transacao: str, valor: float) -> None:
        self.tipo_transacao = tipo_transacao
        self.valor = valor


class ContaBancaria:
    def __init__(self, numero: str) -> None:
        self.numero = numero
        self.saldo = 0
        self.transacoes: list[Transacao] = []

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.transacoes.append(Transacao("Depósito", valor)) # cria um objeto transacao, anotando o tipo que é deposito e o valor do deposito

    def sacar(self, valor: float) -> None:
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.transacoes.append(Transacao("Saque", valor))

    def extrato(self) -> None:
        print(f'Extrato - Conta {self.numero}')

        for transacao in self.transacoes:
            sinal = '+' if transacao.tipo_transacao == 'Depósito' else '-'
            print(f'{transacao.tipo_transacao} {sinal}R$ {transacao.valor:.2f}')
            
        print(f'Saldo: R$ {self.saldo:.2f}\n')


conta = ContaBancaria("1234")
conta.depositar(500)
conta.sacar(120)
conta.extrato()

try:
    conta.sacar(1000)
except ValueError as e:
    print(f"Erro: {e}")