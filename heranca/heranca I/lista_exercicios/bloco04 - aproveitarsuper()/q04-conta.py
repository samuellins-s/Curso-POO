class Conta:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self.saldo = saldo

    def exibir_extrato(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo:.2f}'


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_rendimento: float) -> None:
        super().__init__(titular, saldo)
        if taxa_rendimento < 0:
            raise ValueError('A taxa de rendimento não pode ser negativa!')
        
        self.taxa_rendimento = taxa_rendimento

    def exibir_extrato(self) -> str:
        base = super().exibir_extrato()
        return f'{base}\nTaxa de rendimento: {self.taxa_rendimento}'


poupanca = ContaPoupanca('Ana', 1000, 0.5)
print(poupanca.exibir_extrato())