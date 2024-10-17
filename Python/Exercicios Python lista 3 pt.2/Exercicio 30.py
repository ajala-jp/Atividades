try:      
    num = []

    while True:
        numero = int(input("Informe um número: "))
        if numero >= 0:
            num.append(numero)
        elif numero < 0:
            break

    print("O menor número digitado foi",min(num))
    print("O maior número digitado foi",max(num))

except:
    print("Valor inserido inválido")
    exit()