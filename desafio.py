import textwrap


def menu():
    menu = """
    ============== MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Contas
    [0] Sair

    Insira uma opção: """

    opcao = input(textwrap.dedent(menu))
    return opcao


def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("Valor informado é inválido.")
    else:
        saldo += valor
        extrato += f"DEPÓSITO NO VALOR DE: R$ {valor:.2f}\n"
        print("\nOperação realizada com sucesso!")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("@@@ Operação falhou, você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("@@@ Operação falhou, o valor do saque excedeu o limite. @@@")

    elif excedeu_saques:
        print("@@@ Operação falhou, número de saques excedidos. @@@")

    elif valor <= 0:
        print('@@@ Operação falhou, o valor informado é inválido! @@@')
    else:
        saldo -= valor
        extrato += f"SAQUE NO VALOR DE: R$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso! ===")

    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n================== EXTRATO =====================")
    if not extrato:
        print("Não foram realizadas movimentações!")
    else:
        print(extrato)
    print(f"SALDO: R${saldo:.2f}")
    print("==================================================")


def criar_usuario(usuarios):
    cpf = input("Informa o CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("@@@ Já existe usuário com este CPF! @@@")
        return

    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento dd-mm-yyyy: ")
    endereco = input("Informe seu endereço (Rua - Bairro - Número): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("@@@ Usuário não encontrado, fluxo de criação de conta finalizado! @@@")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            valor = float(input("Insira um valor para depositar: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Insira um valor para sacar: R$ "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada!")


if __name__ == "__main__":
    main()
