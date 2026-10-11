class Musica:
    def __init__(self, nome: str, autor: str, duracao: int) -> None:
        self.nome = nome
        self.autor = autor
        self.duracao = duracao

class Playlist:
    def __init__(self):
        self._lista_musicas: list[Musica] = []

    def adicionar(self, musica: Musica) -> None:
        self._lista_musicas.append(musica)

    def remover(self, musica: Musica) -> None:
        pass

    def duracao_total(self) -> int:
        musica_duracao_total = 0
        for musica in self._lista_musicas:
            musica_duracao_total += musica.duracao

        return musica_duracao_total
        