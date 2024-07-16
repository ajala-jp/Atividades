basemaior = int(input("Digite a base maior do trapézio: "))

if basemaior <= 0:
        basemaior = int(input("Digite a base maior do trapézio novamente: "))

else:

    basemenor = int(input("Digite a base menor do trapézio: "))

    if basemenor <=0:
        basemenor = int(input("Digite a base menor do trapézio novamente: "))
    else:


        altura = int(input("Digite a altura do trapézio: "))

        area = ((basemaior + basemenor)*altura)/2

        print("A área do trapézio é:",area)