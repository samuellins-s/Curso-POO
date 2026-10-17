class Carro:
    def __init__(self, modelo: str, km: int) -> None:
        self.modelo = modelo
        self.km = km

    def __str__(self) -> str:
        return f'{self.modelo} - {self.km} km'


class Motorista:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def dirigir(self, carro: Carro) -> None:
        carro.km += 50
        print(f'{self.nome} dirigiu o {carro.modelo}')


carro = Carro("Fiesta", 1000)
motorista = Motorista("Ana")
print(carro)
motorista.dirigir(carro)
print(carro)