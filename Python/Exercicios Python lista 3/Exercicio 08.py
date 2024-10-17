soma = 0
positivo = 0
for i in range(1,11):
    numero = int(input("Digite um numero: "))
    if numero >= 0:
        soma += numero
        positivo += 1

media = soma / positivo
print(media)