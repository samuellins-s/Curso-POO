class Veiculo:
    def __init__(self):
        pass

    def andar(self) -> str:
        print('O veículo está andando...')


class Carro(Veiculo):
    def abastecer(self) -> str:
        print('O carro está sendo abastecido...')


class CarroEletrico(Carro):
    def carregar(self) -> str:
        print('O carro elétrico está carregando...')


veiculo = Veiculo()
carro = Carro()
c_eletrico = CarroEletrico()

c_eletrico.andar()
