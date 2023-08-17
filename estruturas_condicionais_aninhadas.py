conta_normal = False
conta_universitaria = False

saldo = 1000
saque = 1200
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial')
    else:
        print('Não foi possível realizar o saque, saldo insuficiente')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    else:
        print('Saldo insuficiente!')
else:
    print('Sistema não reconheceu este tipo de conta')
    