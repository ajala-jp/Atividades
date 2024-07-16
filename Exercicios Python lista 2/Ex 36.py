salario = float(input("Informe seu salário: "))
tempo = int(input("Informe a quantos anos está na empresa:"))

if salario <= 500:
    reajuste = salario+((salario*25)/100)
    if tempo >= 1 and tempo <= 3:
        reajuste = reajuste + 100
        print("O salário atual é:",reajuste)

    elif tempo >= 4 and tempo <= 6:
        reajuste = reajuste + 200
        print("O salário atual é:",reajuste)

    elif tempo >= 7 and tempo <= 10:
        reajuste = reajuste + 300
        print("O salário atual é:",reajuste)

    elif tempo > 10:
        reajuste = reajuste + 500
        print("O salário atual é:",reajuste)

elif salario <= 1000:
    reajuste = salario+((salario*20)/100)

    if tempo >= 1 and tempo <= 3:
        reajuste = reajuste + 100
        print("O salário atual é:",reajuste)

    elif tempo >= 4 and tempo <= 6:
        reajuste = reajuste + 200
        print("O salário atual é:",reajuste)

    elif tempo >= 7 and tempo <= 10:
        reajuste = reajuste + 300
        print("O salário atual é:",reajuste)

    elif tempo > 10:
        reajuste = reajuste + 500
        print("O salário atual é:",reajuste)

elif salario <= 1500:
    reajuste = salario+((salario*15)/100)

    if tempo >= 1 and tempo <= 3:
        reajuste = reajuste + 100
        print("O salário atual é:",reajuste)

    elif tempo >= 4 and tempo <= 6:
        reajuste = reajuste + 200
        print("O salário atual é:",reajuste)

    elif tempo >= 7 and tempo <= 10:
        reajuste = reajuste + 300
        print("O salário atual é:",reajuste)

    elif tempo > 10:
        reajuste = reajuste + 500
        print("O salário atual é:",reajuste)

elif salario <= 2000:
    reajuste = salario

    if tempo >= 1 and tempo <= 3:
        reajuste = reajuste + 100
        print("O salário atual é:",reajuste)

    elif tempo >= 4 and tempo <= 6:
        reajuste = reajuste + 200
        print("O salário atual é:",reajuste)

    elif tempo >= 7 and tempo <= 10:
        reajuste = reajuste + 300
        print("O salário atual é:",reajuste)

    elif tempo > 10:
        reajuste = reajuste + 500
        print("O salário atual é:",reajuste)
    