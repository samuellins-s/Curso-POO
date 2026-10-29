from dataclasses import dataclass

@dataclass(order=True)
class Musica:
    duracao_seg: int # vai ser nesta ordem aqui (primeira declaração)
    titulo: str
    artista: str


musicas = [Musica(230, 'Abuabu', 'joka'), Musica(120, 'Jambumba', 'Leozin'), Musica(400, 'Maralto', 'Elioder')]

print(sorted(musicas))