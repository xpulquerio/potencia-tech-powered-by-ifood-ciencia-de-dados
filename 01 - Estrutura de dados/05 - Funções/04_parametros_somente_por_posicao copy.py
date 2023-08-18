def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): #Por posição / por chave-valor
    print(modelo, ano, placa, marca, motor, combustivel)

def criar_carro1(modelo, ano, placa, marca, motor, combustivel): #Por posição
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro1(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
