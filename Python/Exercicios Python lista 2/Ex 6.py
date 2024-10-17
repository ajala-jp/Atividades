turno = str(input("Qual turno você estuda: M, V ou N: "))

if turno == "M" or turno == "m":
    print("Bom dia!")
elif turno == "V" or turno == "v":
    print("Boa tarde!")
elif turno == "N" or turno == "n":
    print("Boa noite!")
else:
    print("Valor inválido")