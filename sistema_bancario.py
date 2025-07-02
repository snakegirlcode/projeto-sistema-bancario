# Sistema Bancário Simples em Python

def menu():
    print("""
========== MENU ==========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Contas
[0] Sair
==========================
""")

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Operação falhou! Valor inválido.")
    return saldo

def sacar(saldo, valor, extrato, limite, saques_realizados, limite_saques):
    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print("❌ Valor do saque excede o limite.")
    elif saques_realizados >= limite_saques:
        print("❌ Limite diário de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:    R$ {valor:.2f}")
        saques_realizados += 1
        print("✅ Saque realizado com sucesso.")
    else:
        print("❌ Operação falhou! Valor inválido.")
    return saldo, saques_realizados

def exibir_extrato(extrato, saldo):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = buscar_usuario(cpf, usuarios)
    if usuario:
        print("❌ Usuário já cadastrado.")
        return
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nasc": data_nasc, "endereco": endereco})
    print("✅ Usuário criado com sucesso.")

def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = buscar_usuario(cpf, usuarios)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"agencia": agencia, "numero": numero_conta, "usuario": usuario})
        print("✅ Conta criada com sucesso.")
    else:
        print("❌ Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        print(f"""\
Agência: {conta['agencia']}
Conta: {conta['numero']}
Titular: {conta['usuario']['nome']}
""")

# === Código principal ===
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = []
saques_realizados = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, saques_realizados = sacar(saldo, valor, extrato, limite, saques_realizados, LIMITE_SAQUES)

    elif opcao == "3":
        exibir_extrato(extrato, saldo)

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        criar_conta(AGENCIA, contas, usuarios)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        print("✅ Encerrando o sistema. Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
