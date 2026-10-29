from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def descreva(self):
        print(f'A área equivale a {self.area()}m\nO perímetro equivale a {self.perimetro()}m')


class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio**2)

    def perimetro(self):
        return 2 * 3.14 * self.raio


class Triagulo(Forma):
    def __init__(self, base, altura, a, b, c):
        self.base = base
        self.altura = altura
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.a + self.b + self.c


retangulo = Retangulo(3, 6)
circulo = Circulo(4)
triangulo = Triagulo(3, 5, 3, 6, 4)

retangulo.descreva()