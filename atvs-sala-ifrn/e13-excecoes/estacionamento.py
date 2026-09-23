class EstacionamentoLotadoError(Exception):
    '''Estacionamento lotado!'''

class Estacionamento:

    vagas_preenchidas = 0

    def __init__(self, vagas_disponiveis):
        self.vagas_disponiveis = vagas_disponiveis

    def entrar(self):
        if self.vagas_preenchidas > self.vagas_disponiveis:
            raise EstacionamentoLotadoError(f'Vagas do estacionamento: {self.vagas_disponiveis} ; Vagas disponiveis: 0')
        
        Estacionamento.vagas_preenchidas += 1