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

    @classmethod
    def quadrado(cls, lado: float) -> "Retangulo":
        return cls(lado, lado)

    @staticmethod
    def eh_valido(base: float, altura: float) -> bool:
        if base <= 0 or altura <=0:
            return False
        return True

print(Retangulo.eh_valido(3, 4))
print(Retangulo.eh_valido(-1, 4))
print(Retangulo.eh_valido(-1, -9))