saldo = 1000
saque = 250
limite = 200
conta_especial = True


x1 = True and True
print("V and V = "+str(x1))
x2 = True and False
print("V and F = "+str(x2))
x3 = False and False
print("F and F = "+str(x3))
x4 = False and True
print("F and V = "+str(x4))

x1 = True or True
print("V or V = "+str(x1))
x2 = True or False
print("V or F = "+str(x2))
x3 = False or False
print("F or F = "+str(x3))
x4 = False or True
print("F or V = "+str(x4))




exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp, exp_2)