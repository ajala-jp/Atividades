print("Qual operações matemáticas gostaria de usar.\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")
equacao = int(input("\nDigite uma das quatro opções acima\n"))

if equacao == 1:
    print("\nVocê escolheu soma")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2

    print("O resultado da soma é:",soma)

elif equacao == 2:
    print("\nVocê escolheu subtração")
    num1 = float(input("Digite o primeiro número"))
    num2 = float(input("Digite o segundo número: "))

    subtracao = num1 - num2
    print("O resultado da subtração é:",subtracao)

elif equacao == 3:
    print("\nVocê escolheu divisão")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    divisao = num1 / num2

    print("O resultado da divisão é:",divisao)

elif equacao == 4:
    print("\nVocê escolheu multiplicação")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    multiplicacao = num1 * num2

    print("O resultado da multiplicação é:",multiplicacao)

else:
    print("Valor inválido")