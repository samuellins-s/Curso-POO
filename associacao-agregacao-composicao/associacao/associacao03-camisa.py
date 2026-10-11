class Camisa:
    def __init__(self, marca: str, cor: str) -> None:
        self.marca = marca
        self.cor = cor

    def apresentar(self):
        print(f'{self.marca} {self.cor}')

class Pessoa:
    def __init__(self, nome: str) -> None:
        self._nome = nome

    def usar_camisa(self, camisa: Camisa) -> None:
        print(f'{self._nome} usando camisa', end=' ')
        camisa.apresentar()


danilo_sinna = Pessoa('Danilo')
camisa_nike = Camisa('Nike', 'Preta')
danilo_sinna.usar_camisa(camisa_nike)