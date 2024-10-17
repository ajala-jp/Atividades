dist = int(input("Digite um numero: "))

if dist > 0:
    for i in range(dist,-1,-1):
        if i % 2 == 0:
            print(i)

else:
    print("Numero inválido, por favor digite um número par.")
