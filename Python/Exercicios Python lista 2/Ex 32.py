idade = int(input("Informe sua idade: "))

if idade >= 5 and idade < 12:
    print("Infantil")

elif idade >= 12 and idade <= 17:
    print("Juvenil")

elif idade > 18:
    print("Sênior")