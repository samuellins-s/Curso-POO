from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa: str, preco_diaria: float) -> None:
        super().__init__()
        self.placa = placa
        self.preco_diaria = preco_diaria

    @abstractmethod
    def calcular_aluguel(self, dias: int) -> float:
        pass

    def descricao(self) -> None:
        print(f'Veículo de Placa: {self.placa} | Preço diária: R$ {self.preco_diaria:.2f}')


class Carro(Veiculo):
    def __init__(self, placa: str, preco_diaria: float) -> None:
        super().__init__(placa, preco_diaria)

    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_diaria * dias


class Moto(Veiculo):
    def __init__(self, placa: str, preco_diaria: float) -> None:
        super().__init__(placa, preco_diaria)

    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_diaria * dias * 0.8 # com desconto de 20%


class Caminhao(Veiculo):
    def __init__(self, placa: str, preco_diaria: float) -> None:
        super().__init__(placa, preco_diaria)

    def calcular_aluguel(self, dias: int) -> float:
            return (self.preco_diaria * dias) + 100


class Locadora:
    def __init__(self, nome_locadora: str) -> None:
        self.nome_locadora = nome_locadora
        self.veiculos: list[Veiculo] = []

    def cadastrar_veiculo(self, veiculo: Veiculo) -> None:
        self.veiculos.append(veiculo)

    ''' Para um faturamento: somas dos calcular_aluguel '''
    def faturamento_previsto(self, dias: int): 
        return sum(veiculo.calcular_aluguel(dias) for veiculo in self.veiculos)


# prova que não pode instanciar (está como coment #):
# veiculo = Veiculo('ABF-2023', 30)
# print(veiculo)
# ERROR DE ABSTRACT CLASS

carrinho = Carro('GKL-8072', 65.90)
motinha = Moto('PWF-9581', 32.85)
caminhaozao = Caminhao('JWQ-2917', 119.99)

locadora = Locadora('Jorginho Locadora')
locadora.cadastrar_veiculo(carrinho)
locadora.cadastrar_veiculo(motinha)
locadora.cadastrar_veiculo(caminhaozao)

print(locadora.faturamento_previsto(2))

for veiculo in locadora.veiculos:
    veiculo.descricao()