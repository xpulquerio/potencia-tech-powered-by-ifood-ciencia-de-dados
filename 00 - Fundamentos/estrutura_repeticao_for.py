texto = ''
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")
    
# range(stop) -> range object
x = list(range(4))
print(x)

# range(start, stop, step) -> range object
a = list(range(1, 10, 1))
print(a)

for numero in range(0, 11):
    print(numero, end=" ")
    
for numero in range(0, 51, 5):
    print(numero, end=" ")