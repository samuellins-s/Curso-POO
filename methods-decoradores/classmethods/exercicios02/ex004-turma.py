class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_texto(cls, texto):
        d, m, a = texto.split('/')
        return cls(int(d), int(m), int(a))

d1 = Data(9, 8, 2026)
d2 = Data.de_texto('09/08/2026')
print(d2)