class Jogo:
    def __init__(self, nome: str, plataforma: str, ano: int) -> None:
        self.nome = nome
        self.plataforma = plataforma
        self.ano = ano
        self.disponivel = True

        self.total_emprestimos = 0

    def __str__(self) -> str:
        return f'{self.nome} ({self.plataforma}, {self.ano}) - {self.disponivel}'

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Jogo):
            return NotImplemented
        return self.nome == outro.nome and self.plataforma == outro.plataforma

if __name__ == '__main__':
    j1 = Jogo('Zelda', 'Switch', 2023, True)
    print(j1)