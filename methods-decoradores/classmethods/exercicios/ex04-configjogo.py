class ConfiguracaoJogo:
    dificuldade = 'normal'

    @classmethod
    def definir_dificuldade(cls, nova_dificuldade):
        cls.dificuldade = nova_dificuldade
        return cls.dificuldade


ConfiguracaoJogo.definir_dificuldade('dificil')
print(ConfiguracaoJogo.dificuldade)

jogador1 = ConfiguracaoJogo()
print(jogador1.dificuldade)