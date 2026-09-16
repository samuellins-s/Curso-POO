class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_texto(cls, texto):
        dia, mes, ano = texto.split('/')
        return cls(int(dia), int(mes), int(ano))

    @staticmethod
    def bissexto(ano):
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def __str__(self):
        return f'{self.dia:02d}/{self.mes:02d}/{self.ano:04d}'
