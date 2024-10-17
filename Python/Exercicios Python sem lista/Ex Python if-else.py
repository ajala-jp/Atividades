A = float(input("Digite o valor de 'A': "))
B = float(input("Digite o valor de 'B': "))
C = float(input("Digite o valor de 'C': "))

if (A > 0):
    if(B > 0):
        print("Tudo ok para decolagem!")
    else:
        print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if(C > 0):
        print("Foguete não tem piloto, mas há outros foguetes disponíveis!")