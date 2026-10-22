class Forma:
    def __init__(self) -> None:
        pass

    def area(self) -> int:
        return 0


class Retangulo(Forma):
    def __init__(self, comp: float, larg: float) -> None:
        super().__init__()
        self.comp = comp
        self.larg = larg

    def area(self) -> float:
        return self.comp * self.larg


class Circulo(Forma):
    def __init__(self, pi: float, raio: float):
        super().__init__()
        self.pi = pi
        self.raio = raio

    def area(self) -> float:
        return self.pi * (self.raio**2)