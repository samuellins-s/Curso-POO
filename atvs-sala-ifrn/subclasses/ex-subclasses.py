class Veiculo:
    def __init__(self, marca, modelo, ano, km_rodados = 0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km_rodados = km_rodados

    def revisar(self):
        self.km_rodados += 1000

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas, tipo_cambio, km_rodados=0):
        super().__init__(marca, modelo, ano, km_rodados)
        self.num_portas = portas
        self.tipo_cambio = tipo_cambio

    def abastecer(self):
        return f'{self.marca} {self.modelo} foi abastecido com SUCESSO!!!'

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada, tipo_moto, km_rodados=0):
        super().__init__(marca, modelo, ano, km_rodados)
        self.cilindrada = cilindrada
        self.tipo_moto = tipo_moto

    def empinar(self):
        return f'{self.marca} {self.modelo} acabou de empinar!!!'

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga, num_eixos, km_rodados=0):
        super().__init__(marca, modelo, ano, km_rodados)
        self.capacidade_carga = capacidade_carga
        self.num_eixos = num_eixos

    def carregar(self):
        return f'{self.marca} {self.modelo} foi carregado com {self.capacidade_carga}kg!!!'

c1 = Carro('Toyota', 'Corolla', 2023, 4, 'Automático')
c1.revisar()
print(c1.abastecer())

m1 = Moto('Honda', 'CB500', 2022, 500, 'Street')
m1.revisar()
print(m1.empinar())

cm1 = Caminhao('Volvo', 'FH', 2020, 15000, 6)
cm1.revisar()
print(cm1.carregar())