from dataclasses import dataclass

@dataclass(frozen=True)
class Endereco:
    rua: str
    numero: int
    cidade: str


casinha = Endereco('Rua Mar', 56, 'João People')
casinha.cidade = 'Natal' # pelo frozen, não consigo