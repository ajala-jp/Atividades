num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2 and num2 < num3:
    print("Crescente")
else:
    print("Não está em ordem crescente")