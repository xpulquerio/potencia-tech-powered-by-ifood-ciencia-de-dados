AGENCIA = '0001'
usuarios = {
    "09984441466" : {
        'nome': 'Ewerson', 
        'data_nascimento': "08/08/1995",
        'endereco': "Av. Wanderley, 107 - Santa Luzia - Penedo/AL",
        'contas': [],
        },
    "00000000000" : {
        'nome': 'João', 
        'data_nascimento': "08/08/1995",
        'endereco': "Rodovia Mario Feary Leahy, 87 - Dom Constantino - Penedo/AL",
        'contas': [1,2],
        }
}
contas = {
    "1" : {
        'conta': 1,
        'agencia': AGENCIA,
        'saldo': 3000.0,
    }, 
    "2" : {
        'conta': 2,
        'agencia': AGENCIA,
        'saldo': 0.0,
    }  
}
def barra_f():
    print("-" * 50)
def barra_g():
    print("=" * 50)
    
def listar_usuarios():
    print("=" * 50)
    print("Lista de Usuários:")
    print("=" * 50)
    for key, usuario in usuarios.items():
        print(f"Usuario {key}: {usuario['nome']}")
        print(f"Contas: {usuario['contas']}")
    print("-" * 50)
def listar_contas_do_usuario(usuario):
    print("=" * 50)
    print("Lista de Contas:")
    print("=" * 50)
    if usuario['contas']:
        for x in usuario['contas']:
            print(x)
            print(f"""Conta: {contas[str(x)]['conta']} | Agência: {contas[str(x)]['agencia']}""")
        print("-" * 50)
    else:
        print(f"{len(usuario['contas'])} - O usuário não possui contas no banco!")
        print("-" * 50)
def cpf_cadastrado(cpf):
    for chave, valor in usuarios.items():
        if chave == cpf:
            return True
    return False

#listar_usuarios()
#listar_contas_do_usuario(usuarios["09984441466"])
#listar_contas_do_usuario(usuarios["00000000000"])


def menu_interno ():
    print("""
    ### MENU ###
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Listar contas
    [q] Sair
    ### ---- ###
    """)
    
def menu_principal ():
    print("""
    ### MENU ###
    [e] Entrar
    [c] Cadastrar usuário
    [a] Cadastrar conta
    [q] Sair
    ### ---- ###
    """)
    
# def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
#     # entrada: saldo, valor, extrato, limite, numero_saques, limite_saques
#     # saída: saldo, extrato
#     pass
# def depsitar(saldo, valor, extrato):
#     # saída: saldo, extrato
#     pass
# def exibir_extrato(saldo, / extrato): #posição / nomeados
#     extrato = f"""
# EXTRATO:
# Conta Corrente: 
# Saldo: R$ {saldo:.2f}
# Saque realizados: {numero_de_saques}
# """
#     print(extrato)
# def cadastrar_usuario():
#     pass
# def criar_conta_corrente():
#     pass



saldo = 0
saque = 0
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
usuarios.get

while True:
    
    menu_principal()
    
    opcao = str(input("Escolha sua opção: "))
    #print(len(opcao))
    if len(opcao) > 1:
        print("Opção indisponível, digite apenas uma letra!")
    else:
        if opcao == "q":
                print("Saindo...")
                break
        elif opcao == "e":
            cpf = str(input("Qual o CPF do Usuário? "))
            if cpf_cadastrado(cpf):
                while True:
                    menu_interno()
                    opcao1 = str(input("Escolha sua opção: "))
                    if opcao1 == "q":
                        print("Saindo...")
                        break
                    elif opcao1 == "d":
                        saldo += float(input(f"Quanto você deseja depositar? "))
                        print(f"Deposito realizado com sucesso!")
                        pass
                    elif opcao1 == "s":
                        if numero_de_saques<LIMITE_DE_SAQUES:
                            saque = float(input(f"Quanto você deseja sacar? "))
                            if saldo >= saque:
                                saldo -= saque
                                print(f"Saque de {saque} realizado com sucesso!")
                                saque = 0
                                numero_de_saques += 1
                            else:
                                print("Saldo insuficiente")
                        else:
                            print("Limite de saques atingido!")
                            
                    elif opcao1 == "e":
                        pass
                    else:
                        print("Opção indisponível, tente novamente!")
            else:
                barra_g()
                print("CPF não encontrado!")
                barra_f()
        elif opcao == 'c':
            cpf = str(input("Qual o CPF do Novo Usuário? "))
            if cpf_cadastrado(cpf):
                print("CPF já existe!")
            else:
                nome_new = str(input("Qual o NOME? "))
                data_nascimento_new = str(input("Qual a DATA DE NASCIMENTO (xx/xx/xxxx)? "))
                #endereco = str(input("Qual o ENDEREÇO (Logradouro, Nº - Bairro - Cidade/(Sigla do Estado))? "))
                usuarios.update({cpf: {'nome': nome_new, 'data_de_nascimento': data_nascimento_new}})
                listar_usuarios()
        elif opcao == 'a':
            cpf = str(input("Qual o CPF do Usuário? "))
            if cpf_cadastrado(cpf):
                listar_contas_do_usuario(usuarios[cpf])
                choice = str(input("Deseja criar uma nova conta, S ou N? "))
                if choice.lower() == 's':
                    temp_key = 0
                    for x in contas.keys():
                        temp_key = int(x)
                    contas.update({str(temp_key+1): {'conta': temp_key+1, 'agencia': AGENCIA, 'saldo':0}})
                    usuarios[cpf]['contas'].append(temp_key+1)
                    print(usuarios[cpf]['contas'])
                else:
                    pass
            else:
                print("Usuário não existe")
        else:
            print("Opção indisponível, tente novamente!")
        
        listar_usuarios()

    
print(f"""Obrigado por usar nosso sistema!""")