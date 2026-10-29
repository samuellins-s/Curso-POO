from dataclasses import dataclass

@dataclass
class Retangulo:
    base: float
    altura: float

    def area(self):
        return self.base * self.altura


ret1 = Retangulo(6, 3)
ret2 = Retangulo(4, 9)
print(ret1.area())

print(ret1)
print(ret1 == ret2)