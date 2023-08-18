AGENCIA = '0001'
usuarios = {
    "1" : {
        'nome': 'Ewerson', 
        'data_nascimento': "08/08/1995",
        'endereco': "Av. Wanderley, 107 - Santa Luzia - Penedo/AL",
        'contas': [],
        },
    "0" : {
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
        'saques': 0,
    }, 
    "2" : {
        'conta': 2,
        'agencia': AGENCIA,
        'saldo': 0.0,
        'saques': 0,
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

def menu_interno ():
    print("""
    ### MENU INTERNO ###
    [l] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ### ---- ###
    """)
    
def menu_principal ():
    print("""
    ### MENU PRINCIPAL ###
    [e] Entrar
    [c] Cadastrar usuário
    [a] Cadastrar conta
    [l] Listar usuários
    [q] Sair
    ### ---- ###
    """)

def depositar (conta, valor):
    contas[str(conta)]['saldo'] += valor
    print(f"Depósito no valor de {valor} - Saldo atualizado: {contas[str(conta)]['saldo']}")

def sacar(*, conta, saque):
    if contas[str(conta)]['saques']<LIMITE_DE_SAQUES:
        if contas[str(conta)]['saldo'] >= saque:
            contas[str(conta)]['saldo'] -= saque
            print(f"Saque no valor de {saque} - Saldo atualizado: {contas[str(conta)]['saldo']}")
            contas[str(conta)]['saques'] += 1
        else:
            print("Saldo insuficiente")
    else:
        print("Limite de saques atingido!")
        
def extrato(conta):
    print(f"""EXTRATO:
Conta Corrente: 
Saldo: R$ {contas[str(conta)]['saldo']:.2f}
Saque realizados: {contas[str(conta)]['saques']}""")

LIMITE_DE_SAQUES = 3

while True:
    #listar_usuarios()
    menu_principal()
    
    opcao = str(input("Escolha sua opção: ")).lower()
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
                    elif opcao1 == "l":
                        listar_contas_do_usuario(usuarios[cpf])
                    elif opcao1 == "d":
                        conta = int(input(f"Qual número da conta? "))
                        if conta in usuarios[cpf]['contas']:
                            valor = float(input(f"Quanto você deseja depositar? "))
                            depositar(conta, valor)                     
                        else:
                            print("Número da conta inválido!")
                    elif opcao1 == "s":
                        conta = int(input(f"Qual número da conta? "))
                        if conta in usuarios[cpf]['contas']:
                            saque = float(input(f"Quanto você deseja sacar? "))
                            sacar(conta=conta, saque=saque)
                        else:
                            print("Número da conta inválido!")
                    elif opcao1 == "e":
                        conta = int(input(f"Qual número da conta? "))
                        if conta in usuarios[cpf]['contas']:
                            extrato(conta=conta)
                        else:
                            print("Número da conta inválido!")
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
                endereco = str(input("Qual o ENDEREÇO (Logradouro, Nº - Bairro - Cidade/(Sigla do Estado))? "))
                usuarios.update({cpf: {'nome': nome_new, 'data_de_nascimento': data_nascimento_new, 'contas': []}})
                #listar_usuarios()
        elif opcao == 'a':
            cpf = str(input("Qual o CPF do Usuário? "))
            if cpf_cadastrado(cpf):
                listar_contas_do_usuario(usuarios[cpf])
                choice = str(input("Deseja criar uma nova conta, S ou N? "))
                if choice.lower() == 's':
                    temp_key = 0
                    for x in contas.keys():
                        temp_key = int(x)
                    contas.update({str(temp_key+1): {'conta': temp_key+1, 'agencia': AGENCIA, 'saldo': 0, 'saques': 0}})
                    usuarios[cpf]['contas'].append(temp_key+1)
                    print(usuarios[cpf]['contas'])
                else:
                    pass
            else:
                print("Usuário não existe")
        elif opcao == 'l':
            listar_usuarios()
        else:
            print("Opção indisponível, tente novamente!")
    
print(f"""Obrigado por usar nosso sistema!""")