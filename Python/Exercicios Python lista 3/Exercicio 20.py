while True:
    num = int(input("Informe um número: "))
    if num == 0:
        break
    elif num % 2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número {num} não é par")
    