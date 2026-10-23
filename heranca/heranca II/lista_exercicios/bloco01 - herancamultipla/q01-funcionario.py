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

robson = Gerente('Robson Farias Melo', '384372824749')
robson.cadastrar_senha('1234')
robson.autenticar('5678')
robson.autenticar('1234')