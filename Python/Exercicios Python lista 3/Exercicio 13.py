dist = int(input("Digite um numero: "))

for i in range(dist,-1,-1):
    print(i)
    

print("..."*148)

cont = dist

while cont >= 0:
    print(cont)
    cont -= 1