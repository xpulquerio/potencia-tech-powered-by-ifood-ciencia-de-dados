saldo = 500
saque = 1000

status = "Sucesso" if saldo >= saque else "Falha"

print (f"{status} ao realizar o saque!")