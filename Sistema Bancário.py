menu = """

[0] Depositar
[1] Sacar 
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu) 
    
    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else: 
             print("Valor informado é inválido, tente novamente!")

          
    elif opcao == "1":
        valor = float(input("Informe o valor do saque que deseja realizar: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente, por favor tente novamente:")

        elif excedeu_limite:
         print("Limite de saque excedido!")     

        elif excedeu_saques:
         print("Limite de saques diários excedidos, por favor tente novamente amanhã!") 

        elif valor > 0: 
         saldo -= valor 
         extrato += f"Saque: R$ {valor: .2f}\n"
         numero_saques += 1

        else:
            print("Operação falhou, o valor informado é inválido") 
         



    elif opcao == "2":
        print("\n===============Extrato================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "3":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
     

        

