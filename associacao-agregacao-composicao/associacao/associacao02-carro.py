'''
pessoa usa carro

'''

class Carro:
    def __init__(self, modelo: str, marca: str) -> None:
        self._modelo = modelo
        self._marca = marca

    def andar(self) -> None:
        print(f'O carro {self._modelo} {self._marca} está andando...')

class Pessoa:
    def __init__(self, nome: str) -> None:
        self._nome = nome

    def dirigir_carro(self, carro: Carro) -> None: # associacao (objeto A entra aqui como parametro)
        print(f'{self._nome} está dirigindo. ', end='')
        carro.andar() # metodo da classe Carro


jorginho = Pessoa('Jorginho')
logan = Carro('Logan', 'Renaut')
logan.andar()
jorginho.dirigir_carro(logan)