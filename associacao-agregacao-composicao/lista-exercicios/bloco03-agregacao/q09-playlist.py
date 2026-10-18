class Musica:
    def __init__(self, nome: str, duracao_seg: int) -> None:
        self.nome = nome
        self.duracao_seg = duracao_seg


class Playlist:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.musicas: list[Musica] = []

    def adicionar(self, musica: Musica) -> None:
        self.musicas.append(musica)

    def duracao_total(self):
        total = sum(musica.duracao_seg for musica in self.musicas )
        return (f'{total:.2f}')

a = Musica("Música A", 180)
b = Musica("Música B", 270)
c = Musica("Música C", 90)

treino = Playlist("Treino")
estudo = Playlist("Estudo")

treino.adicionar(a)
treino.adicionar(b)
estudo.adicionar(b)
estudo.adicionar(c)

for p in (treino, estudo):
    print(f"Playlist {p.nome} ({p.duracao_total()}): {', '.join(m.nome for m in p.musicas)}")

qtd = sum(1 for p in (treino, estudo) if b in p.musicas)
print(f'"{b.nome}" está em {qtd} playlists')