from ex010 import Avaliacao

def main():
    av1 = Avaliacao('Josefabo', 'SOA')
    av1.nota = -7.2
    av1.nota = 3.5
    print(f'{av1.nome} tirou {av1.nota} em {av1.disciplina}')

if __name__ == '__main__':
    main()