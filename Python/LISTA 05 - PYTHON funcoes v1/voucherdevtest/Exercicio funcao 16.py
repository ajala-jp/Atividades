def num(*numeros:float):
    soma = sum(numeros)/len(numeros)
    return soma

x = num(17.3,25.12,63.4)

print(x)