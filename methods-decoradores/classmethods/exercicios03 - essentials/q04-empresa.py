class Empresa:

    nome_empresa = 'Não definido'

    @classmethod
    def renomear_empresa(cls, novo_nome):
        cls.nome_empresa = novo_nome
        return novo_nome

Empresa.renomear_empresa("TechCorp")
print(Empresa.nome_empresa)  # TechCorp

func1 = Empresa()
print(func1.nome_empresa)  # TechCorp