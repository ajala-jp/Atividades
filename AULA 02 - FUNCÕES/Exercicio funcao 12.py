def num(*numeros:int):
    soma = sum(numeros) / len(numeros)
    return soma

x = num(14,1,120,10)

print(x)