try:
    num1 = int(input("Informe o valor inicial: "))
    num2 = int(input("Informe o valor final: "))
    soma = 0

    if num1 > num2:
        print("Intervalo de valores inválidos")
        exit()
    else:
        for i in range(num1, num2+1):
            if i % 2 == 1:
                soma += i

    print(soma)

except:
    exit()

