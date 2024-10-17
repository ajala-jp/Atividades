valor = float(input("Informe o valor da venda:"))

if valor >= 10000000:
    comissao = 700.00 + ((valor * 16)/100)
    print ("O valor da comissão é:",comissao)

if valor < 10000000 and valor >= 8000000:
    comissao = 650.00 + ((valor * 14)/100)
    print ("O valor da comissão é:",comissao)

if valor < 8000000 and valor >= 6000000:
    comissao = 600.00 + ((valor * 14)/100)
    print ("O valor da comissão é:",comissao)

if valor < 6000000 and valor >= 4000000:
    comissao = 550.00 + ((valor * 14)/100)
    print ("O valor da comissão é:",comissao)

if valor < 4000000 and valor >= 2000000:
    comissao = 500.00 + ((valor * 16)/100)
    print ("O valor da comissão é:",comissao)

if valor < 2000000:
    comissao = 400.00 + ((valor * 16)/100)
    print ("O valor da comissão é:",comissao)
