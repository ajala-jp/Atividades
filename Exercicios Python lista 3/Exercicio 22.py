cont = 0
soma = 0
while True:
    nota = float(input("Informe sua nota: "))
    if nota >= 0 and nota <= 10:
        soma += nota
        cont += 1
    elif nota < 0 or nota > 10:
        break


media = soma/cont
print(media)