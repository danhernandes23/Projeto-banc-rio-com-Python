
import textwrap


def menu():

    menu = """\n
  ============MENU============

  [0]\tDepositar
  [1]\tSacar 
  [2]\tExtrato
  [3]\tNova Conta
  [4]\tListar Contas
  [5]\tNovo Usuário
  [6]\tSair
  => """
    return input(textwrap.dedent(menu)) 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Ttitular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "usuario" : usuario}
    print("\n@@@ Usuário não foi encontrado, criação de contas encerrado! @@@")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados [0] if usuarios_filtrados else None 
def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ CPF já registrado por outro usuário! @@@")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome" : nome, "data nascimento" : data_nascimento,"cpf" : cpf, "endereco" : endereco})
    print("\n=== Usuário criado com êxito! ===")    
def exibir_extrato(saldo, /, *, extrato):
     print("\n===============Extrato================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print (f"\nSaldo: R$ {saldo:.2f}")
     print("======================================")
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n@@@ Operação falhou! você não possui saldo suficiente! @@@")

        elif excedeu_limite:
         print("\n@@@  Operação falhou! Limite de saque excedido! @@@")     

        elif excedeu_saques:
         print("\n@@@ Operação falhou! Limite de saques diários excedidos, por favor tente novamente amanhã! @@@") 

        elif valor > 0: 
         saldo -= valor 
         extrato += f"Saque:\t\tR$ {valor: .2f}\n"
         numero_saques += 1
         print("\n=== Saque realizado!! === ")

        else:
            print("\n@@@ Operação falhou, o valor informado é inválido @@@")          
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor: .2f}\n"
        print("\n=== Seu depósito foi realizado com sucesso! ===")
    else:
        print("\n@@@ Depósito faljou! O valor informado é inválido. @@@")

    return saldo,extrato
def main():
 
 LIMITE_SAQUES=3
 AGENCIA= "0001"

 saldo= 0
 limite= 500
 extrato= ""
 usuarios= []
 contas= []
 
 while True:
    opcao = menu() 
    
    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        saldo,extrato = depositar(saldo,valor,extrato)
          
    elif opcao == "1":
        valor = float(input("Informe o valor do saque que deseja realizar: "))

        saldo,extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "2":
       exibir_extrato(saldo, extrato=extrato)

    elif opcao == "5":
        criar_usuario(usuarios)

    elif opcao == "3":
        numero_conta=len(contas) +1
        conta = criar_conta(AGENCIA, numero_conta, usuarios) 

    elif opcao == "4":
        listar_contas(contas) 

    elif opcao == "6":
     break  

    else:
     print("Operação inválida, por favor insira novamente a operação desejada.")

main()

     

