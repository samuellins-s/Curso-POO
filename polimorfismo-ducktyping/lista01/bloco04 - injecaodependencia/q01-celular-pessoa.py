'''
Vou criar uma injeção de dependencia onde a Pessoa só consegue existir se um Celular já existir.
    Vou fazer essa relação criando primeiro a classe Celular e definir seus métodos.
    Após isso, vou criar a classe Pessoa e no seu construtor ser injetado um parametro de type Celular, virando obrigatorio a existencia do Celular primeiro para a Pessoa ser instanciada.
'''

class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, msg: str) -> None:
        print(f'Enviando a mensagem: "{msg}"')

    def abrir_emails(self) -> None:
        print('Abrindo os emails...')

    def abrir_youtube(self) -> None:
        print('Abrindo o YouTube...')


class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.celular = celular # injeção de dependencia (objeto Celular entrando como atributo)

    def pedir_pizza(self) -> None:
        print('Vou pedir uma pizza...')
        print(f'Pegando o meu {self.celular.modelo}')
        print('Abrindo o WhatsApp...')
        self.celular.enviar_mensagem('Olá, boa noite! Quero pedir uma pizza G de Mussarela!')
        print('Aguardando a pizza...')

    def estudar(self) -> None:
        print('Vou estudar agora...')
        print(f'Pegando o meu {self.celular.modelo}...')
        self.celular.abrir_youtube()
        print('Anotando o conteúdo...')


android = Celular('Samsung')
iphone = Celular('Iphone 15 Pro')

jorginho = Pessoa(android)
jorginho.pedir_pizza()
print()
jorginho.estudar()