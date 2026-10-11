'''
Uma associação é moldada pelo relacionamento de uso.
    Pessoa usa interruptor
    Pessoa usa teclado
    Pessoa usa camisa

A. define o objeto a ser usado
    define seu metodo de ativação

B. quem irá usar o objeto A
    recebe o objeto A como parametro de metodo -> associacao
    utiliza o metodo do A

'''

class Interruptor:
    def __init__(self, comodo: str) -> None:
        self._comodo = comodo

    def acender(self) -> None:
        print(f'Acendendo: {self._comodo}')

class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def acender_interruptor(self, interruptor: Interruptor) -> None:
        print(f'{self.nome}: ', end='')
        interruptor.acender()


maria = Pessoa('Maria')
sala = Interruptor('Sala')
maria.acender_interruptor(sala)