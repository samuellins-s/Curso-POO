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

    def __str__(self) -> str:
        return f'Retângulo {self.base}x{self.altura}'

    def __repr__(self) -> str:
        return f'Retangulo(base={self.base}, altura={self.altura})'

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

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Retangulo):
            return NotImplemented
        return self.base == outro.base and self.altura == outro.altura

    def __lt__(self, outro) -> bool:
        return self.calcular_area() < outro.calcular_area()

lista = [Retangulo(5, 5), Retangulo(2, 2), Retangulo(3, 3)]
for retangle in sorted(lista):
    print(retangle)
# deve sair em ordem crescente (pelo critério que você definiu)