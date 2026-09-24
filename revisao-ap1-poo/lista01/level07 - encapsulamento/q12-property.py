class ContaBancaria:
    def __init__(self, saldo: float, senha: str) -> None:
        self.saldo = saldo
        self.__senha = senha

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            raise ValueError('Digite um saldo positivo!')
        self._saldo = valor

c = ContaBancaria(100, "1234")
c.saldo = 200
print(c.saldo)   # 200

try:
    c.saldo = -50
except Exception as e:
    print("Erro:", e)  # não deve aceitar saldo negativo