from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria

    def calcular_valor_aluguel(self, dias):
        return dias * self.valor_diaria

    def info(self):
        return f'Placa: {self.placa} ; Modelo: {self.modelo} ; Ano: {self.ano}'

    @abstractmethod
    def verificar_categoria(self):
        pass

class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, num_portas, combustivel):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.num_portas = num_portas
        self.combustivel = combustivel

    def abastecer(self):
        return f'O carro foi abastecido com {self.combustivel} litros'

    def verificar_categoria(self):
        if self.num_portas >= 4:
            return 'Executivo'
        else:
            return 'Popular'

class Moto(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, cilindrada):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.cilindrada = cilindrada

    def empinar(self):
        return 'Empinando a moto'

    def verificar_categoria(self):
        if self.cilindrada > 500:
            return 'Alta Cilindrada'
        else:
            return 'Popular'

class Caminhao(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, capacidade_carga):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_carga = capacidade_carga

    def carregar(self, peso):
        if peso <= self.capacidade_carga:
            return f'O peso {peso}T cabe com sucesso na capacidade {self.capacidade_carga}T do caminhão!'
        else:
            return f'O peso {peso}T NÃO cabe na capacidade {self.capacidade_carga}T do caminhão!'

    def verificar_categoria(self):
        return 'Utilitario'