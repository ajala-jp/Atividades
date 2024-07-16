nota1 = float(input("Digite sua primeira nota: "))
nota1 = nota1 * 2
nota2 = float(input("Digite sua segunda nota: "))
nota2 = nota2 * 3
nota3 = float(input("Digite sua terceira nota: "))
nota3 = nota3 * 5

if nota1 <= 10 or nota1 >= 0 or nota2 <= 10 or nota2 >= 0 or nota3 <= 10 or nota3 >= 0:
    media = (nota1 + nota2 + nota3)/10
    print("Sua média foi: ",media)
    if media < 3:
        print("Reprovado")
    
    elif media > 3 and media < 6:
        print("Recuperação")
    else:
        print("Aprovado")

 