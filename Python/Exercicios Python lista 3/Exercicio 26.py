num1 = int(input("Informe um número base: "))
num2 = int(input("Informe um número expoente: "))
multi = 1

for i in range(num2):
    multi *= num1

print(multi)