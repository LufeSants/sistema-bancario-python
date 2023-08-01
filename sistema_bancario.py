menu = """\033[36m
888888b.                                                        
888  "88b                                                       
888  .88P                                                       
8888888K.   8888b.  88888b.   .d8888b .d88b.  88888b.  888  888 
888  "Y88b     "88b 888 "88b d88P"   d880088b 888 "88b 888  888 
888    888 .d888888 888  888 888     88800888 888  888 888  888 
888   d88P 888  888 888  888 Y88b.   Y880088P 888 d88P Y88b 888 
8888888P"  "Y888888 888  888  "Y8888P "Y88P"  88888P"   "Y88888 
                                              888           888 
                                              888      Y8b d88P 
                    [1] - Depositar           888       "Y88P"               
                    [2] - Sacar
                    [3] - Extrato 
                    [4] - Sair
______________________________________________________________         
=>\033[m """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito R$: "))

        if valor > 0:
            saldo += valor
            print("\033[1;30;42mDepósito feito com sucesso!\033[m")
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\033[1;30;41mOperação falhou! o valor informado é inválido.\033[m")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque R$: "))

        excedeu_saldo = valor > saldo

        excedeu_limite  = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo: 
            print("\033[1;30;41mOperação falhou! Você não tem saldo suficiente.\033[m")

        elif excedeu_limite:
            print("\033[1;30;41mOperação falhou! O valor do saque excedeu o limite.\033[m")

        elif excedeu_saque: 
            print("\033[1;30;41mOperação falhou! número máximo de saques excedido.\033[m")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("\033[1;30;42mSaque feito com sucesso!\033[m")
            numero_saques += 1

        else:
            print("\033[1;30;41mOperação falhou! o valor informado é inválido.\033[m")

    elif opcao == "3":
        print("\n================= EXTRATO =================")
        print("\033[1;37;43mNão foram realizadas movimentações.\033[m" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("\033[1;30;41mOperação inválida, por favor selecione novamente a operação desejada.\033[m")