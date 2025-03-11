from datetime import datetime

def criar_usuario(usuario):
    nome = input("Entre seu nome completo: ")
    data_nasc = (input("Informe sua data de nascimento (dia / mês / ano): "))
    cpf = input("Entre seu CPF: ")
    endereco = input("Informe seu endereço: ")

    datetime.strptime(data_nasc, '%d/%m/%Y')

    if cpf not in usuario:
        novo_usuario = (f"Nome: {nome}\nData de Nascimento: {data_nasc}\nEndereço: {endereco}\n")
        usuario[cpf] = novo_usuario
        print("Usuário cadastrado com sucesso!\n")
    else:
        print("Usuário já cadastrado.\n")
        return

def criar_conta(usuario, conta):
    saldo = 0
    cpf = input("Informe ceu CPF: ")

    if cpf in usuario:
        num_conta = "0001" + "-" + str((len(conta)+1)) + "-" + cpf
        conta[num_conta] = [saldo, cpf]
        print(f"Conta {num_conta} criada com sucesso!\n")

    else:
        print("Usuário não cadastrado.\n")

def deposito(valor:float, num_conta:str, conta, operacoes:list):
    if valor > 0:
        conta[num_conta][0] = conta[num_conta][0] + valor
        operacoes.append(f"Valor de R${valor} reais depositado na conta {num_conta}.")
        print(f"Operação realizada com sucesso!\n")
        return True
    
    else:
        print("Valor de depósito deve ser maior que zero.\n")
        return False

def saque(valor:float, num_conta:str, num_saque_diario:int, conta, operacoes:list):
    if valor > 0 and valor <= 500 and num_saque_diario < 3:

        if valor <= conta[num_conta][0]:
            conta[num_conta][0] = conta[num_conta][0] - valor
            num_saque_diario += 1
            operacoes.append(f"Valor de R${valor} sacado da conta {num_conta}.")
            print(f"Operação realizada com sucesso!\n")
            return True
        
        else:
            print("Saldo insuficiente.\n")
            return False
    
    else:
        print("Impossível realizar esta operação.\n")
        return False
    
def extrato(conta, operacoes:list, num_conta:str):
    print("\n========== EXTRATO ===========\n")

    if(operacoes):
        for el in operacoes:
            print(el)
    else:
        print("Nenhuma operação executada hoje.")

    print(f"Saldo atual: R${round(conta[num_conta][0],2)}")

    print("\n==============================\n")

def listar_contas(conta):
    i = 0
    for el in conta:
        i += 1
        print(f"Conta {i}: {el}")
    print("\n")

def main():
    usuario = {}
    conta = {}
    operacoes = []
    num_saque_diario = 0

    while True:
        escolha = input("Qual operação deseja executar?\n[s] SAQUE\n[d] DEPÓSITO\n[e] EXTRATO\n[c] CRIAR CONTA\n[u] CADASTRAR USUÁRIO\n[l] LISTAR CONTAS\n[q] SAIR\n")

        if escolha == 'u':
            criar_usuario(usuario=usuario)

        elif escolha == 'c':
            criar_conta(usuario=usuario, conta=conta)

        elif escolha == 's':
            num_conta = input("Informe o número de sua conta: ")

            if num_conta in conta:
                ver = saque(num_conta=num_conta, valor=float(input("Informe o valor: ")), num_saque_diario=num_saque_diario, conta=conta, operacoes=operacoes)

                if ver:
                    num_saque_diario += 1
                else:
                    continue

            else:
                print("Conta não existe.")

        elif escolha == 'd':
            num_conta = input("Informe o número de sua conta: ")

            if num_conta in conta:
                deposito(num_conta=num_conta, valor=float(input("Informe o valor: ")), conta=conta, operacoes=operacoes)
            else:
                print("Conta não existe.")

        elif escolha == 'e':
            num_conta = input("Informe o número de sua conta: ")

            if num_conta in conta:
                extrato(conta=conta, operacoes=operacoes, num_conta=num_conta)
            else:
                print("Conta não existe.")

        elif escolha == 'l':
            listar_contas(conta)

        else:
            break

main()