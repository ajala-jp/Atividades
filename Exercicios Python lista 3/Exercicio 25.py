soma = 0
cont = 0
while True:
    num = int(input("Informe sua idade: "))
    if num != 0:
        soma+=num
        cont +=1
    elif num == 0:
        break
media = soma/cont
print(media)