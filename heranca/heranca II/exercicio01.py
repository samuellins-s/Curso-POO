class Funcionario:
    def __init__(self, nome: str, matricula: float) -> None:
        self._nome = nome
        self._matricula = matricula

    # nome
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome_novo: str) -> None:
        if nome_novo == '':
            raise ValueError
        if nome_novo == self._nome:
            raise ValueError
        self._nome = nome_novo

    # martricula
    @property
    def matricula(self) -> float:
        return self._matricula
    
    @matricula.setter
    def matricula(self, nova_matricula: float) -> None:
        if nova_matricula == '':
            raise ValueError
        if nova_matricula == self._matricula:
            raise ValueError
        self._matricula = nova_matricula


class Autenticavel:
    def __init__(self, senha: str) -> None:
        self._senha = senha
    
    def atualizar_senha(self, senha: str) -> None:
        pass

