class Jogo:
    def __init__(self, nome: str, plataforma: str, ano: int) -> None:
        self.nome = nome
        self.plataforma = plataforma
        self.ano = ano
        self.disponivel = True

    def __str__(self) -> str:
        disponivel = ''
        if self.disponivel:
            disponivel = 'disponivel'
        else:
            disponivel = 'emprestado'
        return f'{self.nome} ({self.plataforma}, {self.ano}) - {disponivel}'

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Jogo):
            raise NotImplemented
        return self.nome == outro.nome and self.plataforma == outro.plataforma


jogo1 = Jogo('Zelda', 'Nintendo Switch', 2023)
print(jogo1.nome, jogo1.plataforma, jogo1.ano, jogo1.disponivel)
jogo1.disponivel = False

jogo2 = Jogo('Call of Duty', 'PC', 2018)
print(jogo2.nome, jogo2.plataforma, jogo2.ano, jogo2.disponivel)

print(jogo1)
print(jogo2)