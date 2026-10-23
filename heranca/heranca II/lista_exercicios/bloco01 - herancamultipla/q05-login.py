class Funcionario:
    def __init__(self, nome: str, matricula: str) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'Sou {self.nome} de matrícula {self.matricula}'

class Autenticavel:
    def __init__(self) -> None:
        self._senha = ''

    def cadastrar_senha(self, nova_senha: str) -> None:
        if self._senha == nova_senha:
            raise ValueError('Coloque uma senha nova diferente da antiga.')
        
        self._senha = nova_senha

    def autenticar(self, senha: str) -> bool:
        return self._senha == senha # bool mesmo


class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome, matricula) -> None:
        Funcionario.__init__(self, nome, matricula)
        Autenticavel.__init__(self)

    def __str__(self) -> str:
        base = super().__str__()
        return f'Cargo Gerente: {base}'

class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome, matricula) -> None:
        Funcionario.__init__(self, nome, matricula)
        Autenticavel.__init__(self)

    def emitir_relatorio(self) -> None:
        print('Relatório: blablabla')

    def __str__(self) -> str:
        base = super().__str__()
        return f'Cargo Diretor: {base}'


class Cliente(Autenticavel):
    def __init__(self, nome: str) -> None:
        Autenticavel.__init__(self)
        self.nome = nome

    def __str__(self):
        return f'Sou {self.nome}'


def login(usuario: Autenticavel, senha: str) -> bool:
    return usuario.autenticar(senha)


gerente = Gerente('Jorjão', '304023424')
diretor = Diretor('Kuka', '859043802')
cliente = Cliente('Marianha')

galerinha: list = [gerente, diretor, cliente]

for pessoa in galerinha:
    if isinstance(pessoa, Funcionario):
        print(pessoa.matricula)

gerente.cadastrar_senha('1234')
diretor.cadastrar_senha('abcd')
cliente.cadastrar_senha('9999')

for usuario, senha in zip(galerinha, ['1234', 'errada', '9999']):
    if login(usuario, senha):
        print(f'{usuario.nome}: acesso liberado')
    else:
        print(f'{usuario.nome}: acesso negado')