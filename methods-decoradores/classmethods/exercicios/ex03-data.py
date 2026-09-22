class Data:
    def __init__(self, dia, mes, ano):
        self.dia, self.mes, self.ano = dia, mes, ano

    @classmethod
    def a_partir_de_texto(cls, texto):
        dia, mes, ano = texto.split('/')
        return cls(int(dia), int(mes), int(ano))

d1 = Data.a_partir_de_texto('20/10/2007')
print(d1.dia, d1.mes, d1.ano)