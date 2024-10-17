numero = int(input("Digite um número: "))
lista = []
if numero > 0:
    for i in range(numero):
        lista.append(i)
    print(sum(lista))