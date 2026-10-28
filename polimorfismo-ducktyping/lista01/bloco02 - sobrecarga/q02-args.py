class Calculadora:
    def __init__(self):
        pass

    def somar(self, *args):
        return sum(args)


calculadora = Calculadora()
print(calculadora.somar(1, 2, 3, 4))


class Notificador:
    def __init__(self):
        pass

    def enviar(self, msg, copia=None):
        print(msg)
        if copia != None:
            print(copia)


notif = Notificador()
notif.enviar('Olá, eu sou a msg')
notif.enviar('Olá de novo! eu sou a msg', 'Olá de novo! eu sou a CÓPIA da msg')

