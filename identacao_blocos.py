def sacar(valor):
    saldo = 500
    
    if saldo >= valor: 
        print('Valor sacado!')
        print('retire o seu dinheiro na boca do caixa.')
    
    print ("Obrigado por ser nosso cliente, tenha um bom dia!")
        
        
def depositar(valor):
    saldo = 500
    saldo += valor

depositar(1000)
sacar(1000)