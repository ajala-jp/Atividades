num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número número: "))
soma = 0
if num2 < num1:
    print("Número inválido!")
else:
    for i in range(num1,num2):
        if i % 2 ==1:
            soma += i

print(soma)