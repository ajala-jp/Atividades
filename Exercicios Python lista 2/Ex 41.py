A = int(input("Digite o valor de 'A': "))
B = int(input("Digite o valor de 'B': "))
C = int(input("Digite o valor de 'C': "))

delta = B**2 - (4*A*C)

print(delta)

if delta < 0:
    print("Não existe raiz")
elif delta == 0:
    print("Raiz única")

else: 

    #Primeira raiz
    raiz1 = (-B + delta**0.5)/(2*A)
    print("Primeira raiz:",raiz1)

    #Segunda raiz
    raiz2 = (-B - delta**0.5)/(2*A)
    print("Segunda raiz:",raiz2)



