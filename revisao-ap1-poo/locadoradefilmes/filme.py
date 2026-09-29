class Filme:
    def __init__(self, titulo: str, ano: int) -> None:
        self.titulo = titulo
        self.ano = ano
        self.disponibilidade_locacao = True

    def __str__(self) -> str:
        disponibilidade = 'disponível' if self.disponibilidade_locacao else 'não disponível'
        return f'{self.titulo} ({self.ano}) - {disponibilidade}'

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Filme):
            return NotImplemented
        return self.titulo == outro.titulo and self.ano == outro.ano


if __name__ == '__main__':
    filme1 = Filme('De volta para o Futuro', 1970)
    print(filme1)

    filme2 = Filme('Vingadores: Ultimato', 2018)

    filme3 = Filme('De volta para o Futuro', 1970)

    print(filme1 == filme3)
    print(filme1 == filme2)

    print(filme2)