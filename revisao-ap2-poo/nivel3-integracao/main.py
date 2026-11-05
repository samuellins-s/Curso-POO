from entregador import DeBike, DeMoto
from restaurante import Restaurante, Pedido, Cliente

def main():
    jorginho_entregas = DeMoto('Jorginho')
    rest_plaza = Restaurante('Plaza')
    pedido1 = Pedido(jorginho_entregas)


if __name__ == '__main__':
    main()