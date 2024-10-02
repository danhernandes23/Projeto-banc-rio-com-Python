#PROJETO BANCARIO 2.0
from abc import ABC, abstractmethod, abstractproperty 
from datetime import datetime, date, timedelta
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)    

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
        def __init__(self, nome, endereco, data_nascimento, cpf):
            super().__init__(endereco)
            self.nome = nome
            self.data_nascimento = data_nascimento
            self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self. numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
    
     @property
     def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo: 
            print("\n@@@ Operação falhou! você não possui saldo suficiente! @@@")
        elif valor > 0:
            self.saldo -= valor
            print("\n=== Saque realizado!! === ")
        else: 
         print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
        return False
    
    def depositar(saldo, valor, extrato, /):
        if valor > 0:
             self.saldo += valor 
             print("\n=== Seu depósito foi realizado com sucesso! ===")
        else:
              print("\n@@@ Depósito faljou! O valor informado é inválido. @@@")
              return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self,limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
            transacoes if transacao ["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

         
        if excedeu_limite:
            print("\n@@@  Operação falhou! Limite de saque excedido! @@@")
        
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Limite de saques diários excedidos, por favor tente novamente amanhã! @@@")
        
        else:
         return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C\C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self.transacoes = []
    
    @property  
    def transacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__nome__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__ (self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    @property
    def valor (self):
        return self.valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
   menu = """\n
  ============MENU============
  [0]\tDepositar
  [1]\tSacar 
  [2]\tExtrato
  [3]\tNova Conta
  [4]\tListar Contas
  [5]\tNovo Cliente
  [6]\tSair
  => """         
   return input(textwrap.dedent(menu))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "0":
            depositar(clientes)
        elif opcao == "1":
            sacar(clientes)
        elif opcao == "2":
            exibir_extrato(clientes)
        elif opcao == "3":
            numero_conta = len(contas)+1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "4":
            listar_contas(contas)
        elif opcao == "5":
            criar_cliente(clientes)
        elif opcao == "6":
            break 
main ()

def depositar(clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_usuario(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito que deseja realizar: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)    
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not  cliente.contas:
        print("\n@@@ Você ainda não é nosso cliente @@@")
        return

    #FIXME: nao permite o cliente escolher a conta
    return cliente.contas[0]

def sacar(clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque que deseja realizar: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)    
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)    
    if not conta:
        return

    print("\n============ EXTRATO ============")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("=================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente (cpf, clientes)

    if cliente:
        print("\n@@@ Já existe um cliente com este CPF @@@")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento =  input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Insira o seu endereço (logradouro, numero - bairro - cidade/sigla do estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n===== Você agora é nosso cliente! =====")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
     print("\n@@@ Usuário não foi encontrado, criação de contas encerrado! @@@")
     return 

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(contas)

    print("\n===== Conta criada com sucesso!! =====")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

