num = []

for i in range(10):
    numero = float(input("Digite um número: "))
    num.append(numero)

print(num)
print("O menor número da lista é: ",min(num))
print("O maior número da lista é: ",max(num))

print("..."*73)

lista = []

while len(lista) < 10:
    lista2 = float(input("Digite um número: "))
    lista.append(lista2)
    if len(lista) == 10:
        break

print(lista)
print("O menor número da lista é: ",min(lista))
print("O maior número da lista é: ",max(lista))