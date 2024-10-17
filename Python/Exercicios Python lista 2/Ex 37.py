fabrica = float(input("Informe o custo de fábrica: "))

if fabrica <= 12000:
    distribuidor = (fabrica * 5)/100
    print("A comissão do distribuidor é: ")

elif fabrica >= 12000 and fabrica <= 25000:
    distribuidor = (fabrica * 10)/100

    imposto = (fabrica * 15)/100

    print("A comissão do distribuidor é:",distribuidor)
    print("E o imposto é de:",imposto)

elif fabrica > 25000:
    distribuidor = (fabrica * 15)/100

    imposto = (fabrica * 20)/100

    print("A comissão do distribuidor é:",distribuidor)
    print("E o imposto é de:",imposto)