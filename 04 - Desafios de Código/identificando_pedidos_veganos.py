numPedidos = int(input())

def eHvegano(x):
    if x == "s":
        return "Vegano"
    else:
        return "Nao-vegano"
pedidos = {}
for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = str(input())
    pedidos.update({
        i : {
            'prato': prato,
            'calorias': calorias,
            'ehVegano': ehVegano},
        })
    
for key, valor in pedidos.items():
    print(f"Pedido {key}: {valor['prato']} ({eHvegano(valor['ehVegano'])}) - {valor['calorias']} calorias")
#TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.