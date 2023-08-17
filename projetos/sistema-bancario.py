menu = """
### MENU ###
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
### ---- ###
"""
saldo = 0
saque = 0
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
extrato = f"""Saldo: R$ {saldo:.2f}
Saque realizados: {numero_de_saques}"""

while True:
    
    print(menu)
    
    opcao = str(input("Escolha sua opção: "))
    #print(len(opcao))
    if len(opcao) > 1:
        print("Opção indisponível, digite apenas uma letra!")
    else:
        if opcao == "q":
            print("Saindo...")
            break
        elif opcao == "d":
            saldo += float(input(f"Quanto você deseja depositar? "))
            print(f"Deposito realizado com sucesso!")
            pass
        elif opcao == "s":
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
                
        elif opcao == "e":
            print(extrato)
        else:
            print("Opção indisponível, tente novamente!")
            
    
print(f"""Obrigado por usar nosso sistema!""")