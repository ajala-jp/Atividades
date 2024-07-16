nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))
nota3 = nota3 * 2

if nota1 > 100 or nota1 < 0 or nota2 > 100 or nota2 < 0 or nota3 > 100 or nota3 < 0:
    print("Nota inválida")
else:
    media = (nota1 + nota2 + nota3)/4
    print(media)
    if media >= 60:
        print("Aprovado")
    else:
        print("Reprovado")

