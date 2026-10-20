'''
1. Universidade e Curso: composição -> pois a Universidade tem cursos (posse), mas um curso não pode existir isoladamente da universidade

2. Livro e Capitulo: composição -> pois um livro tem capitulos. um capitulo depende de um livro existir

3. Empresa e Funcionario: agregação -> pois uma empresa tem funcionarios. ambos existem indepedentemente

4. Carro e Motor: composição -> pois um carro tem motor. o motor depende do carro existir. 

5. Usuario e Endereco: agregação -> pois um usuario possui um endereco. ambos existem indepedentemente

6. Musico e Banda: agregação -> pois uma banda tem musicos. ambos existem independentemente

'''

# 6. Musico e Banda
class Musico:
    def __init__(self, nome: str, instrumento: str) -> None:
        self.nome = nome
        self.instrumento = instrumento

    def tocar(self) -> str:
        return f'{self.nome} está tocando {self.instrumento}...!'


class Banda:
    def __init__(self, nome: str, genero: str) -> None:
        self.nome = nome
        self.genero = genero
        self.musicos: list[Musico] = []

    def adicionar_musico(self, musico: Musico) -> None:
        self.musicos.append(musico)

    def remover_musico(self, musico: Musico) -> None:
        self.musicos.remove(musico)

    def ver_musicos_componentes(self) -> None:
        for musico in self.musicos:
            print(f'{musico.nome} --- {musico.instrumento}')

    def comecar_musica(self) -> None:
        print('\n1, 2, 3, e...!')
        for musico in self.musicos:
            print(musico.tocar())

    def __str__(self) -> str:
        return f'Nome da banda: {self.nome} --- Gênero musical predominante: {self.genero}'


# jorginho = Musico('Jorginho', 'Trompete')
# print(jorginho.tocar())

# danilo = Musico('Danilo Sinna', 'Saxofone Tenor')

# macedo = Musico('Macedo Alves', 'Trombone')

# banda_redencao = Banda('Banda Redenção', 'Samba')
# print(banda_redencao)

# banda_redencao.adicionar_musico(jorginho)
# banda_redencao.adicionar_musico(danilo)
# banda_redencao.adicionar_musico(macedo)
# banda_redencao.ver_musicos_componentes()
# banda_redencao.comecar_musica()

# 2. Livro e Capitulo
class Capitulo:
    def __init__(self, numero: int, titulo: str, texto: str) -> None:
        self.numero = numero
        self.titulo = titulo
        self.texto = texto

class Livro:
    def __init__(self, titulo: str, autor: str, ano_lancamento: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_lancamento = ano_lancamento
        self.capitulos: list[Capitulo] = []

    def escrever_capitulo(self, numero: int, titulo: str, texto: str) -> None:
        self.capitulos.append(Capitulo(numero, titulo, texto)) # criacao do objeto e append
        print(f'Capítulo {numero}. "{titulo}" criado com SUCESSO!')

    def remover_capitulo(self, numero_capitulo: int) -> None:
        for capitulo in self.capitulos:
            if numero_capitulo == capitulo.numero:
                self.capitulos.remove(capitulo)
                print(f'Capítulo de número {capitulo.numero} removido com SUCESSO!')

            else:
                print(f'Capítulo de numero {capitulo.numero} NÃO encontrado!')

    def ver_capitulos(self) -> None:
        for capitulo in self.capitulos:
            print(f'Capítulo: {capitulo.numero}. {capitulo.titulo}')

    def __str__(self) -> str:
        return f'Título do livro: {self.titulo} --- Autor: {self.autor} --- Ano de lançamento: {self.ano_lancamento}'


# vamaislonge = Livro('Vá mais longe', 'Augusto Cury', 2021)
# print(vamaislonge)

# vamaislonge.escrever_capitulo(1, 'Desvendando os papéis e os segredos da memoria', 'blablablablablabla....')
# vamaislonge.escrever_capitulo(2, '10 técnicas para proteger a memória', 'blublublublublublu...')
# vamaislonge.remover_capitulo(2)

# vamaislonge.ver_capitulos()

class Curso:
    def __init__(self, nome: str):
        self.nome = nome


class Universidade:
    pass
