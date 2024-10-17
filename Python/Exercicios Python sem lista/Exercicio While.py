numero = int(input("Digite um numero: "))

lista = []
for o in range (0,100):
    lista.append(o)

cont = 0

while cont < len(lista):
    print(lista[cont])
    if lista[cont] == numero:
        print("Encontramos o número",numero)
        break
    else:
        cont = cont + 1

print("Fim do programa")
