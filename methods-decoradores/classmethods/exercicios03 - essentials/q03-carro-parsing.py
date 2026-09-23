class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca, self.modelo, self.ano = marca, modelo, ano

    @classmethod
    def a_partir_de_texto(cls, texto):
        marca, modelo, ano = texto.split('-')
        return cls(marca, modelo, ano)

c = Carro.a_partir_de_texto("Fiat-Uno-2015")
print(c.marca, c.modelo, c.ano)  # Fiat Uno 2015