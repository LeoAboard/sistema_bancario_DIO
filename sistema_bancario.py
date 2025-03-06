saldo = 0
operacoes = []
num_saque_diario = 0

def deposito():
    global saldo
    valor = float(input("Entre o valor de depósito:\n"))

    if valor > 0:
        saldo = saldo + valor
        operacoes.append(f"Valor de R${valor} reais depositado.")
        print(f"Operação realizada com sucesso!\n")
        return True
    
    else:
        print("Valor de depósito deve ser maior que zero.\n")
        return False
    
def saque():
    global num_saque_diario
    global saldo
    valor = float(input("Entre o valor de saque:\n"))

    if valor > 0 and valor <= 500 and num_saque_diario < 3:

        if valor <= saldo:
            saldo = saldo - valor
            num_saque_diario += 1
            operacoes.append(f"Valor de R${valor} sacado.")
            print(f"Operação realizada com sucesso!\n")
            return True
        
        else:
            print("Saldo insuficiente.\n")
            return False
    
    else:
        print("Impossível realizar esta operação.\n")
        return False
    
def extrato():
    global saldo

    print("========== EXTRATO ===========\n")

    if(operacoes):
        for el in operacoes:
            print(el)
    else:
        print("Nenhuma operação executada hoje.")

    print(f"Saldo atual: R${round(saldo, 2)}")

    print("\n==============================")

while True:
    escolha = input("Qual operação deseja executar?\n[s] SAQUE\n[d] DEPÓSITO\n[e] EXTRATO\n[q] SAIR\n")

    if escolha == 's':
        saque()

    elif escolha == 'd':
        deposito()

    elif escolha == 'e':
        extrato()

    else:
        break