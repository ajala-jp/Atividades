numero = int(input("Digite um número: "))
cont = 0
if numero > 100 and numero < 9999:
        num=str(numero)

        while cont < len(num):
            print(num[0+cont])
            cont += 1 
else:
      print("Numero inválido")

