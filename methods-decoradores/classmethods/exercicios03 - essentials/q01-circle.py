class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @classmethod
    def a_partir_de_diametro(cls, diametro):
        raio = diametro / 2
        return cls(raio) # constutor alternativo que retorna objeto -> com cls(arg)

c1 = Circulo(5)
c2 = Circulo.a_partir_de_diametro(10)
print(c2.raio)