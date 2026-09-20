class Casa:

    lista = []

    def __init__(self, qtd_quartos, qtd_banheiros, qtd_vagas):
        self.qtd_quartos = qtd_quartos
        self.qtd_banheiros = qtd_banheiros
        self.qtd_vagas = qtd_vagas

        Casa.lista.append(self)

    def __repr__(self):
        return f'A casa possui {self.qtd_quartos} quartos, {self.qtd_banheiros} banheiros e {self.qtd_vagas} vagas'

    @classmethod
    def filtro_qtd_quartos(cls, qtd_quartos):
        lista_casas_filtro = []

        for casa in Casa.lista:
            if casa.qtd_quartos >= qtd_quartos:
                lista_casas_filtro.append(casa)

        return lista_casas_filtro

    @classmethod
    def filtro_qtd_banheiros(cls, qtd_banheiros):
        lista_casas_filtro = []
        for casa in Casa.lista:
            if casa.qtd_banheiros >= qtd_banheiros:
                lista_casas_filtro.append(casa)

        return lista_casas_filtro

casa1 = Casa(3, 2, 2)
casa2 = Casa(5, 4, 3)
casa3 = Casa(1, 1, 1)

print(Casa.lista)
print(Casa.filtro_qtd_quartos(3))
print(Casa.filtro_qtd_banheiros(4))