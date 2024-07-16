numero = int(input("Digite um numero: "))
i = 0

for item in range(numero*2):
    if item % 2 == 1:
        print(item)

print("..."*148)

while i < numero*2:   
    i += 1
    if i % 2 == 1:
        print(i)
    
