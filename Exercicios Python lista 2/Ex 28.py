print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números")
opcao = int(input("\nDigite uma das quatro opções acima\n"))
if opcao <= 0 or opcao > 4:
    print("Opção inválida")

else:

 if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2
    print("O resultado da soma é:",soma)

 elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if num1 > num2:
        sub = num1 - num2
        print("O resultado da subtração é:",sub)

    else:
        sub = num2 - num1
        print("O resultado da subtração é:",sub)

 elif opcao == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    multi = num1 * num2

    print("O resultado do produto entre esses dois números é:",multi)

 elif opcao == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        num2 = float(input("Digite o segundo número: "))
    else:
        divisao = num1 / num2

        print("O resultado da divisão é:",divisao)
            
