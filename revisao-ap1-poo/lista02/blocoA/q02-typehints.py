class Jogo:
    def __init__(self, nome: str, plataforma: str, ano: int) -> None:
        self.nome = nome
        self.plataforma = plataforma
        self.ano = ano
        self.disponivel = True


jogo1 = Jogo('Zelda', 'Nintendo Switch', 2023)
print(jogo1.nome, jogo1.plataforma, jogo1.ano, jogo1.disponivel)

jogo2 = Jogo('Call of Duty', 'PC', 2018)
print(jogo2.nome, jogo2.plataforma, jogo2.ano, jogo2.disponivel)
