ano = int(input("Digite um ano: "))

resto = ano % 4

if resto == 0:
    print("Ano bissexto")
else:
    print("Não é ano bissexto")