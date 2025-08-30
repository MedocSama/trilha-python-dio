menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operacao invalida! Selecione outra opção!!!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operacao falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operacao falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operacao falhou! Numero maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operacao falhou! Valor invalido.")

    elif opcao == "e":
        print("\n==================== Extrato ====================")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================================")

    elif opcao == "q":
        break
        
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")