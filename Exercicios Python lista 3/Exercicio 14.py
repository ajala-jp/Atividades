dist = int(input("Digite um numero: "))

if dist > 0:
    for i in range(0,dist+1,1):
        if i % 2 == 0:
            print(i)
else:
   print("Número inválido")

