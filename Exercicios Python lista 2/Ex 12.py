num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    diferenca = num1 - num2 
    print("O número",num1,"é maior que o número",num2,"e a diferença entre eles é: ",diferenca)
else:
    diferenca = num2 - num1 
    print("O número",num2,"é maior que o número",num1,"e a diferença entre eles é: ",diferenca)