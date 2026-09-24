'''
O certo é validar antes de atribuir.
    Eu havia feito o contrario... eu recebi os valores do init e depois que eu validei.
    
Correto:
    1. Valido o valor recebido
    2. Atribuo ou não o valor recebido

'''

class Retangulo:
    def __init__(self, base: float, altura: float) -> None:

        # validacao
        if base <= 0:
            raise ValueError('Valor menor que 0 (zero)!')
        
        if altura <= 0:
            raise ValueError('Valor menor que 0 (zero)!')

        # passando da validacao, atribuir os valores
        self.base = base
        self.altura = altura

        
try:
    r3 = Retangulo(-1, 4)
except Exception as error:
    print('Erro:', error)