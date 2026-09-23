class Temperatura:
    def __init__(self, temperatura):
        self.temperatura = temperatura # em celcius

    @property
    def fahrenheit(self):
        return self.temperatura * 9/5 + 32 # conversao celcius -> fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, valor):
        valor = (valor - 32) * 5/9
        self.temperatura = valor
        
t = Temperatura(0)
print(t.fahrenheit)  # esperado: 32.0

t.fahrenheit = 212
print(t.temperatura)  # esperado: 100.0