class Jogador:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Time:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.jogadores: list[Jogador] = []

    def adicionar_jogador(self, jogador: Jogador) -> None:
        self.jogadores.append(jogador)

    def remover_jogador(self, jogador: Jogador) -> None:
        if jogador not in self.jogadores:
            raise ValueError('Remova um jogador disponível')
        self.jogadores.remove(jogador)


neymar = Jogador("Neymar")
pedro = Jogador("Pedro")
caio = Jogador("Caio")
time = Time("Raio FC")

time.adicionar_jogador(neymar)
time.adicionar_jogador(pedro)
time.adicionar_jogador(caio)
print(f"Time {time.nome}: {', '.join(j.nome for j in time.jogadores)}")

time.remover_jogador(pedro)
print(f"Removido: {pedro.nome}")
print(f"Time {time.nome}: {', '.join(j.nome for j in time.jogadores)}")
print(f"Pedro continua existindo: {isinstance(pedro, Jogador)}")