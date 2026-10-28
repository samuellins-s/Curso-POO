class Forma:
    def __init__(self) -> None:
        pass

    def area(self) -> float:
        return 0


class Retangulo(Forma):
    def __init__(self, base: float, altura: float) -> None:
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura


class Circulo(Forma):
    def __init__(self, raio: float) -> None:
        super().__init__()
        self.raio = raio

    def area(self) -> float:
        return 3.14 * (self.raio**2)


class Triangulo(Forma):
    def __init__(self, base: float, altura: float) -> None:
        super().__init__()
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return (self.base * self.altura) / 2


def area_total(formas: list[Forma]):
    return sum(forma.area() for forma in formas)


formas = [Retangulo(6, 2), Circulo(5), Triangulo(3, 5)]
print(area_total(formas))