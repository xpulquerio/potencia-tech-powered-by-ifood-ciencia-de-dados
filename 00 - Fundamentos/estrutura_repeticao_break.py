opcao = -1

while True:
    opcao = int(input("Informe um número: "))
    
    if opcao == 10:
        print('Bye!')
        break
    
    print(opcao)

for numero in range(100):
    if numero == 12:
        break
    print(numero, end=" ")

print(10)

for numero in range(100):
    if numero % 2 == 0: #Se o número for "par" pule (continue)
        continue
    print(numero, end=" ")
    
#continue - Pular
#break - Parar