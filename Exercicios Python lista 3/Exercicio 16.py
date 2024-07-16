dist = int(input("Digite um numero: "))

if dist > 0 and dist % 2 == 1:  
    for i in range(0,dist,1):
        if i % 2 == 1:
            print(i)

else:
    print("Numero inválido, por favor digite um número ímpar.")
