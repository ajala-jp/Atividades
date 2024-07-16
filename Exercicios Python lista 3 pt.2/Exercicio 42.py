while True:
    num = int(input("Informe um número: "))
    if num <= 0:
        print(f"Você digitou o número {num}, iremos encerrar o sistema.")
        break
    else:
        quadrado = num ** 2
        cubo = num ** 3
        raiz = num ** 0.5
        print(f"O valor do número {num} ao quadrado é: {quadrado} ")
        print(f"O valor do número {num} ao cubo é: {cubo} ")
        print(f"A raiz do número {num} é: {raiz:.2f} ")
