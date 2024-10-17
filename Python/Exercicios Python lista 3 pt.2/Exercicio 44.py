try:
    while True:
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Saída")

        print("Escolha uma das opções acima para poder continuar")
        opcao = int(input())
        if opcao == 1:
            print("Você escolheu a opção de ADIÇÃO!\n")

            num1 = float(input("Informe o valor do primeiro número: "))
            num2 = float(input("Informe o valor do segundo número: "))
            soma = num1 + num2
            print(f"A soma dos números digitados é {soma}\n")
            continue
        
        elif opcao == 2:
            print("Você escolheu a opção de SUBTRAÇÃO!\n")

            num1 = float(input("Informe o valor do primeiro número: "))
            num2 = float(input("Informe o valor do segundo número: "))
            sub = num1 - num2
            print(f"A subtração dos números digitados é {sub}\n")
        
        elif opcao == 3:
            print("Você escolheu a opção de MULTIPLICAÇÃO!\n")

            num1 = float(input("Informe o valor do primeiro número: "))
            num2 = float(input("Informe o valor do segundo número: "))
            multi = num1 * num2
            print(f"A multiplicação dos números digitados é {multi}\n")
        
        elif opcao == 4:
            print("Você escolheu a opção de DIVISÃO!\n")
            
            num1 = float(input("Informe o valor do primeiro número: "))
            num2 = float(input("Informe o valor do segundo número: "))
            div = num1 / num2
            print(f"A divisão dos números digitados é {div}\n")
        
        elif opcao == 5:
            print("Encerrando o programa.")
            break
        else:
            print(" Número Inválido\n Por favor, escolha novamente\n")

except:
    print("Valor inválido")

