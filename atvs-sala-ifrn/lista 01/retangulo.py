class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f'Área do retangulo: {self.base * self.altura}'

    def perimetro(self):
        return f'Perímetro do retangulo: {(2 * self.base) + (2 * self.altura)}'

    def __eq__(self, other):
        if not isinstance(other, Retangulo):
            return NotImplemented
        return self.base == other.base and self.altura == other.altura