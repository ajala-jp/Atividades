num = int(input("Informe um número: "))
multi = 1
cont = 0
while True:
    multi *= num
    num -= 1  
    if cont == num:
        break
print(multi)
    

