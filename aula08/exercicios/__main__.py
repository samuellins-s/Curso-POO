from veiculos import Carro, Moto, Caminhao

def main():
    carro1 = Carro('fez-3740', 'Civic', 2012, 300, 4, 30)
    print(carro1.info())
    print(carro1.verificar_categoria())
    print(carro1.abastecer())

    moto1 = Moto('QYP-5936', 'Bros', 2015, 150, 160 )
    print(moto1.calcular_valor_aluguel(7))
    print(moto1.empinar())

    caminhao1 = Caminhao('JBH-7205', 'Jubarte', 2018, 760, 2)
    print(caminhao1.carregar(2))

if __name__ == '__main__':
    main()