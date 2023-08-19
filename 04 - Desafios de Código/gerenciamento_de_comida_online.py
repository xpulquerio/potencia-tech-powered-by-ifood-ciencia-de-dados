def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
    return total
#TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).
 
 
if __name__ == "__main__":
    total = main()
    
    per = str(input())
    if per == "10%":
        total *= 0.90
        print(f"Valor total: {total:.2f}")
    elif per == "20%":
        total *= 0.80
        print(f"Valor total: {total:.2f}")