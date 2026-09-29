class Jogo:
    def __init__(self, nome: str, plataforma: str) -> None:
        self.nome = nome
        self.plataforma = plataforma


jogo1 = Jogo('Zelda', 'Nintendo Switch')
print(jogo1.nome, jogo1.plataforma)

jogo2 = Jogo('Call of Dutty', 'PC')
print(jogo2.nome, jogo2.plataforma)
