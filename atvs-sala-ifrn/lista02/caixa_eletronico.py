import math

from atvlista02 import ContaBancaria, ErroDeConta


def ler_inteiro(mensagem):
    """Lê um inteiro; retorna None se a entrada for inválida."""
    try:
        return int(input(mensagem).strip())
    except ValueError:
        return None


def ler_valor(mensagem):
    """Lê um valor monetário (aceita vírgula); None se inválido."""
    try:
        valor = float(input(mensagem).strip().replace(',', '.'))
    except ValueError:
        return None
    # float() aceita 'nan' e 'inf', que corromperiam o saldo
    return valor if math.isfinite(valor) else None


def exibir_menu():
    print(
        '\n========= MENU CAIXA ELETRÔNICO =========\n'
        'Criar conta [1]\n'
        'Ver saldo da conta [2]\n'
        'Fazer depósito na conta [3]\n'
        'Fazer saque [4]\n'
        'Sair [0]\n'
    )


def criar_conta():
    numero = input('Número da conta: ').strip()
    if not numero:
        print('O número da conta não pode ser vazio.')
        return None

    titular = input('Nome do titular: ').strip()
    if not titular:
        print('O nome do titular não pode ser vazio.')
        return None

    texto = input('Saldo inicial (Enter para R$ 0,00): ').strip()
    saldo = 0
    if texto:
        saldo = ler_valor_de_texto(texto)
        if saldo is None:
            print('Saldo inicial inválido.')
            return None

    conta = ContaBancaria(numero, titular, saldo)  # pode levantar ErroDeConta
    print('Conta criada com sucesso!')
    print(conta)
    return conta


def ler_valor_de_texto(texto):
    try:
        valor = float(texto.replace(',', '.'))
    except ValueError:
        return None
    return valor if math.isfinite(valor) else None


def main():
    conta = None

    while True:
        exibir_menu()

        try:
            opcao = ler_inteiro('Digite qual número deseja acessar: ')

            if opcao is None:
                print('Digite um número válido.')
                continue

            if opcao == 0:
                print('Encerrando o caixa eletrônico. Até logo!')
                break

            elif opcao == 1:
                nova = criar_conta()
                if nova is not None:
                    conta = nova

            elif opcao in (2, 3, 4):
                if conta is None:
                    print('Crie uma conta primeiro (opção 1).')
                    continue

                if opcao == 2:
                    print(conta)

                elif opcao == 3:
                    valor = ler_valor('Valor do depósito: R$ ')
                    if valor is None:
                        print('Digite um valor numérico válido.')
                        continue
                    conta.depositar(valor)
                    print(f'Depósito realizado. Saldo: R$ {conta.saldo:.2f}')

                else:
                    valor = ler_valor('Valor do saque: R$ ')
                    if valor is None:
                        print('Digite um valor numérico válido.')
                        continue
                    conta.sacar(valor)
                    print(f'Saque realizado. Saldo: R$ {conta.saldo:.2f}')

            else:
                print('Digite um número válido.')

        except ErroDeConta as erro:
            # Cobre ValorInvalidoError, SaldoInsuficienteError e LimiteExcedidoError
            print(f'Operação não realizada: {erro}')

        except (KeyboardInterrupt, EOFError):
            print('\nEntrada interrompida. Voltando ao menu.')

        except Exception as erro:
            print(f'Erro inesperado: {erro}')


if __name__ == '__main__':
    main()