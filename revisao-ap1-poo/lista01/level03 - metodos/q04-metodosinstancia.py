class Retangulo:
    def __init__(self, base: float, altura: float) -> None:

        # validacao
        if base <= 0:
            raise ValueError('Base deve ser maior que zero!')
        
        if altura <= 0:
            raise ValueError('Altura deve ser maior que zero!')

        # passando da validacao, atribuir os valores
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

r4 = Retangulo(3, 4)
print(r4.calcular_area())
print(r4.calcular_perimetro())