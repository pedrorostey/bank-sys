# v1: apenas um usuario
# sistema de banco com
# deposito de valores exibidos no extrato
# saque com 3 saques diarios com limite de 500 exibidos no extrato
# R$ 1500.45 modelo de exibiçao

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
valor = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float (input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    
        else:
            print("O valor informado é inválido!")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float (input("Informe o valor do saque: "))

            if valor > 0:
                    
                if valor <= limite:    

                    if valor <= saldo:

                        saldo -= valor
                        extrato += f"Saque: R$ {valor:.2f}\n"
                        numero_saques += 1

                    else:
                        print("Saldo insuficiente!")
                else:
                    print("O valor informado excede o limite da operação!")    
            else:
                print("O valor informado é inválido!")        
        else:
            print("Número máximo de saques excedidos!")        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor tente novamente a operação desejada.")