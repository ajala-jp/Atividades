num = int(input("Informe um número: "))
soma = 0

for i in range(1,num-1):
    if num % i == 0:
        soma += i
print(soma)