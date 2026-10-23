class Funcionario:
    def __init__(self, nome: str, matricula: str) -> None:
        self.nome = nome
        self.matricula = matricula


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


class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome, matricula) -> None:
        Funcionario.__init__(self, nome, matricula)
        Autenticavel.__init__(self)

    def emitir_relatorio(self) -> str:
        pass


class Cliente(Autenticavel):
    def __init__(self, nome: str) -> None:
        Autenticavel.__init__(self)
        self.nome = nome


gerente = Gerente('Fabao', '324023048904')
funcionario = Funcionario('Funcionario generico', '0')
cliente = Cliente('Jorginho')

print(isinstance(gerente, Funcionario)) # gerente é um funcionario
print(isinstance(gerente, Autenticavel)) # gerente é um autenticavel
print(isinstance(cliente, Funcionario)) # cliente não é um funcionario