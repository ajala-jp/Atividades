num1 = int(input("Digite o primeiro número números: "))
num2 = int(input("Digite o segundo número números: "))
soma = 0
multi = 1
for i in range(num1):
    if i % 2 == 0:
        soma += i
        
    else:
        multi *= i
        
print("..."*148)

for i in range(num2):
    if i % 2 == 0:
        soma += i
        
    else:
        multi *= i

soma += num1 + num2
print("A soma dos números pares é: ",soma)
print("A multiplicação dos números ímpares é: ",multi)

