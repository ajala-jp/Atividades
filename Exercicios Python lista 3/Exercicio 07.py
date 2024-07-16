soma = 0
for i in range(1,11):
    numero = int(input("Digite um numero: "))
    soma += numero

media = soma / i
print(media)

print(".-"*73)

soma2 = 0
cont = 0

while cont < 10:
    num = int(input("Digite um numero: "))
    soma2 += num
    cont += 1

media = soma2 / cont
print(media)