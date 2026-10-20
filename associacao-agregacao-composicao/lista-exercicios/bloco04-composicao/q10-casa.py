class Comodo:
    def __init__(self, nome: str, area: float) -> None:
        self.nome = nome
        self.area = area


class Casa:
    def __init__(self, endereco: str, comodos: list[Comodo]) -> None:
        self.endereco = endereco
        self.comodos = comodos
        for comodo in self.comodos:
            self.comodos.append(comodo)
        
    def area_total(self):
        for nome, area in self.comodos:
            total = sum(area)