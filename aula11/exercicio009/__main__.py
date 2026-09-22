from ex009 import Avaliacao

def main():
    av1 = Avaliacao('Jorginho', 'POO')
    print(av1.get_nota()) # pego o valor

    av1.set_nota(4) # altero o valor
    av1.set_nota(-2) # altero o valor (INVÁLIDO)
    print(av1.get_nota())

if __name__ == '__main__':
    main()