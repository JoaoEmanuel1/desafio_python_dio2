menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
numero_saques = 0

while True:
    print(menu)
    opcao = int(input("Informe uma opção: "))

    if opcao == 1:

        valor_deposito = float(input("\nDigite o valor para depositar: R$ "))

        if valor_deposito <= 0:
            print("Valor informado é inválido.")

        else:
            saldo += valor_deposito
            extrato += f"DEPÓSITO NO VALOR DE: R$ {valor_deposito:.2f}\n"
            print("\nOperação realizada com sucesso!")

    elif opcao == 2:

        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número de saques diários excedido.")

        else:
            valor_saque = float(input("Digite o valor para sacar: R$ "))

            if valor_saque <= 0 or valor_saque > 500:
                print("Valor de saque inválido!")

            elif valor_saque > saldo:
                print("Você não possui saldo suficiente!")

            else:
                saldo -= valor_saque
                extrato += f"SAQUE NO VALOR DE: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print("\nOperação realizada com sucesso!")

    elif opcao == 3:

        print("\n==================== EXTRATO ====================\n")

        if not extrato:
            print("Não foram realizadas movimentações!")

        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        
        print("==================================================")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
