quantidade = int(input("Digite uma quantidade de numero que deseja acrescentar: "))
lista = []
for i in range(quantidade):
    numeros = float(input("Digite um número: "))
    lista.append(numeros)
print("O maior número digitado foi:",max(lista))