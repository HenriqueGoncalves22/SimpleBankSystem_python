menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
"""

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    deposito = float(input("Digite o valor do Depósito: "))
    if deposito > 0:
        saldo += deposito
        extrato += f"Deposito realizado com o valor de: R${deposito:.2f}\n"
    else:
        print("Valor Inválido")

#Permitir até 3 saques por dia

def sacar():
    global saldo, extrato, limite, numero_saques, LIMITE_SAQUES
    saque = float(input("Digite o valor do Saque: "))

    if saque > limite:
        print("Operação Cancelada! Ultrapassou o limite")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação Cancelada! Ultrapassou o limite de saques diários")
    elif saque > saldo:
        print("Operação Cancelada! Saldo Insuficiente")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque realizado com o valor de: R${saque:.2f}\n"
        numero_saques += 1
    else:
        print("Valor Inválido")


#Exibir os depositos, saques e o saldo atual
def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "d":
        depositar()

    elif opcao == "s":
        sacar()

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        print("Sair..")
        break

    else:
        print("Operação Inválida, selecione uma opção dentro da lista")


