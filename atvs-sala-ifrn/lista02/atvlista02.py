'''
Nível 02
Aplicação - Cadastro com validação

'''

# 6. Funcionario
class SalarioInvalidoError(Exception):
    '''Valor menor que o salário mínimo!'''

class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, valor: float) -> None:
        salario_minimo = 1621
        if valor < salario_minimo:
            raise SalarioInvalidoError('Digite um valor maior que o salário mínimo!')
        self._salario = valor

    def aumentar(self, percentual: float) -> None:
        if not (0 < percentual <= 30):
            raise ValueError('Apenas valores entre 0 e 30!')
        self._salario = self._salario + (percentual/100 * self._salario)

try:
    f1 = Funcionario('Jupeba', 2300)
    f1.salario = 1200
except SalarioInvalidoError as error:
    print(f'Salário menor que Salário Mínimo: {error}')

# --------------------------------------------------------------------------------------

# 7. Email
class EmailInvalidoError(Exception):
    '''Email em caracteres "@" e "."'''

class Email:
    def __init__(self, endereco: str) -> None:
        self.endereco = endereco

    @property
    def endereco(self) -> str:
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        if '@' not in endereco or '.' not in endereco:
            raise EmailInvalidoError('Digite “@” e “.”')
        self._endereco = endereco

try:
    e1 = Email('samuel.lins@escolar.ifrn.edu.br')
    e1.endereco = 'semnadapapai'
except EmailInvalidoError as error:
    print(f'Endereço errado... {error}')

# --------------------------------------------------------------------------------------

'''
Nível 03
Integração — Caixa eletrônico

'''

# 9. ContaBancaria
class ErroDeConta(Exception):
    '''Erro de Conta!'''

class ValorInvalidoError(ErroDeConta):
    '''Valor inválido!'''

class SaldoInsuficienteError(ErroDeConta):
    '''Saldo insuficiente!'''

class LimiteExcedidoError(ErroDeConta):
    '''Limite de saque excedido!'''


class ContaBancaria:
    def __init__(self, numero: str, titular: str, saldo:float = 0) -> None:
        self.numero_da_conta = numero
        self.titular = titular
        self.saldo = saldo

    def __str__(self) -> str:
        return f'Informações da Conta Bancária:\nTitular: {self.titular}\nNumero da conta: {self.numero_da_conta}\nNúmero da conta: {self.numero_da_conta}'

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValorInvalidoError('Digite um valor maior que zero (0)!')
        self._saldo = valor

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteError('Digite um valor válido. Ultrapassou o saldo disponível')

        limite_saque = 1000
        if valor > limite_saque:
            raise LimiteExcedidoError(f'Digite um valor menor que R${limite_saque}!')

        self._saldo -= valor