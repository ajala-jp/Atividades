def consumoaparelho(potencia,tempo):
    consumo = (potencia * tempo)/1000
    return consumo


def calculoconta(consumo, valor:float = 28.84):
    valorconta = consumo * valor
    return valorconta


valorconta = calculoconta(consumo=consumoaparelho(300,8))

print(valorconta)