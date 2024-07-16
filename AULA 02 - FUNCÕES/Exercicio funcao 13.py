def valores(quantidade, valor):
    lista= []
    for item in range(quantidade):
        lista.append(valor)
    return lista

x = valores(5,"A")

print(x)