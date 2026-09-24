class ContaBancaria:
    def __init__(self, saldo: float, senha: str) -> None:
        self._saldo = saldo
        self.__senha = senha

c = ContaBancaria(100, "1234")
print(c._saldo)         # 100 -> funciona, mas é "convenção", não deveria acessar assim de fora
print(c.__senha)        # deve dar AttributeError (name mangling)