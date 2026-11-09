from entregador import DeBike, DeMoto
from restaurante import Restaurante, Prato, Cardapio, Pedido, Item, Cliente

def main():
    hotdog = Prato('Cachorro-Quente', 1, 5.90)
    cardapio = Cardapio()
    cardapio.adicionar_prato(hotdog)

    cachorro_quente_da_7 = Restaurante('Cachorro Quente da 7')

    item1 = Item(hotdog, 2)
    print(item1.subtotal())

    jorginho_entregas = DeMoto('Jorginho')

    rafael = Cliente('Rafael Castro')
    print(rafael.nome)

    pedido1 = Pedido(jorginho_entregas)
    pedido1.adicionar_item(item1)
    pedido1.total(10, rafael)


if __name__ == '__main__':
    main()