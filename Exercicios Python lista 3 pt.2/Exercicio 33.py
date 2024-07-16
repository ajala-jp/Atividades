try:
    lista_num = []

    for i in range (10):
        num = int(input("Informe um número: "))
        lista_num.append(num)

    digito_usuario = int(input("Digite um valor: "))

    if digito_usuario in lista_num:
        print(f"O valor digitado, {digito_usuario} está no vetor!")

    else:
        print(f"O valor digitado, {digito_usuario} não está no vetor")

except:
    print("Valor inválido")