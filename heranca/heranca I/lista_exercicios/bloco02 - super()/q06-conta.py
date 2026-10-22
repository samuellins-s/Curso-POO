class Conta:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self.saldo = saldo


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_rendimento: float) -> None:
        super().__init__(titular, saldo)
        if taxa_rendimento < 0:
            raise ValueError('A taxa de rendimento não pode ser negativa!')
        
        self.taxa_rendimento = taxa_rendimento


continha = ContaPoupanca('Jorginho', 8049, 20)
print(continha.taxa_rendimento)