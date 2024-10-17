def volume():
    altura = float(input("Informe a altura: "))
    raio = float(input("Informe o raio: "))
    pi = 3.141592
    volume =  pi*raio**2*altura
    return volume

print(volume())