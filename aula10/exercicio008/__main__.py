from ex008 import ContaBancaria

# sem proteção alguma... 

def main():
    c1 = ContaBancaria(111, 'Joãofina', 5000)
    c1.depositar(500)
    c1.saldo_conta = 0 # está privado, não deixa...
    c1._nome_titular = 'Petero' # titular é protegido.. petero fica em atributo novo 

    print(c1)

if __name__ == '__main__':
    main()