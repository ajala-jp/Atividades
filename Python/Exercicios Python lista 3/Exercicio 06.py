soma = 0
for i in range(10):
    numero = float(input("Digite um número: "))
    soma += numero

print(soma)


print("--"*20)


cont = 0
soma2 = 0
while cont < 10:
    num = float(input("Digite um número: "))
    cont += 1
    soma2 += num
    if cont == 10:
        break
print(soma2)