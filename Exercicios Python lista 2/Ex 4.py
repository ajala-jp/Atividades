num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))
num3 = float(input("Digite o valor do terceiro número: "))

if num1 < num2 and num2 < num3:
    print("Os números estão em ordem crescente:",num1,"|", num2,"|",num3)
else:
    print("Os números não estão em ordem crescente")