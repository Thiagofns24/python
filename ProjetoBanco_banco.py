from typing import List
from time import sleep

from ModelsBanco.cliente import Cliente
from ModelsBanco.conta import Conta

contas: List[Conta] = []


def main() -> None:
    """

    :rtype: object
    """
    menu()


def menu() -> None:
    print('==========================')
    print('======== ATM =============')
    print('====== Nu Bank ==========')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 -  Efetuar depósito')
    print('4 - Efeturar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()


def criar_conta() -> None:
    """

    :rtype: object
    """
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do cliente:')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)  # adicionamos a lista de contas

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('-----------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:  # len - retorna o comprimento de um objeto
        numero: int = int(input('Informe o numero da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:  # Se a conta for encontrada, informar valor
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com número {numero}')

    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))  # O = numero de origem

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino:'))  # D = conta destino

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_o.transferir(conta_d, valor)

            else:
                print(f'A conta destino com número {numero_d} não foi encontrada.')

        else:
            print(f'A sua conta com número {numero_o} não foi encontrada.')



    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:  # para cada conta dentro da nossa lista, imprima conta
            print(conta)
            print('-----------------')
            sleep(1)
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
