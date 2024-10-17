try:
    while True:
        r1 = float(input('Informe o valor do resistor 1: '))
        r2 = float(input('Informe o valor do resistor 2: '))
        if r1 == 0 or r2 == 0:
            break
        res = (r1 * r2)/(r1+r2)
        print(res)
    
except:
    print("Valor inserido inválido!")
    