class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @classmethod
    def quadrado(cls, lado):
        return cls(int(lado), int(lado))

r1 = Retangulo(4, 5)
r2 = Retangulo.quadrado(3)
print(r2.largura, r2.altura)