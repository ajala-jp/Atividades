valor  = float(input("Digite o valor da aquisição do produto: "))

if valor < 50 or valor < 50.0:
    valormaior = (valor * 45) / 100
    valortotal = valor + valormaior
    print("O valor do produto será: ",valortotal)
elif valor == 50:
    valormaior = (valor * 30)/100
    valortotal = valor + valormaior
    print("O valor do produto será: ",valortotal)
else:
    valormaior = (valor * 30)/100
    valortotal = valor + valormaior
    print("O valor do produto será: ",valortotal)

