def consumo(distancia, litro):
    consumo = distancia/litro
    if consumo < 8:
        print("Gasta muito!")
    elif consumo >= 8 and consumo <= 15:
        print("Econômico!")
    elif consumo > 15:
        print("Super econômico!")

consumo(1000,70)