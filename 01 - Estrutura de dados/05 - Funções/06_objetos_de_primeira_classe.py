def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

def test (a, b):
    x = somar(a,b)
    print(f"Soma na nova função é {x}")
    
test(10, 20)
