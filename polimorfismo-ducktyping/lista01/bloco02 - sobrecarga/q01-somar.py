class Calculadora:
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b

    def somar(self, a, b, c): # esse metodo somar sobescreveu o primeiro. python não tem sobrecarga de metodos
        return a + b + c


calculadora = Calculadora()
calculadora.somar(1, 2)
