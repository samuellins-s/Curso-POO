class Pessoa:
    especie = 'Homo Sapiens'

    @classmethod
    def mostrar_especie(cls):
        print(f'Todos são da especie: {cls.especie}')

Pessoa.mostrar_especie()

