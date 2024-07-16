preco = float(input("Digite o preço do produto: "))
print("1 - MG")
print("2 - SP")
print("3 - RJ")
print("4 - MS")
estado = int(input("Digite qual opção de estado será enviado: "))

if estado <= 0 or estado > 4:
    print("Valor inválido")

else:

    if estado == 1:
        taxa = (preco * 7)/100
        total = taxa + preco
        print("O preço final ficou:",total)

    elif estado == 2:
        taxa = (preco * 12)/100
        total = taxa + preco
        print("O preço final ficou:",total)

    elif estado == 3:
        taxa = (preco * 15)/100
        total = taxa + preco
        print("O preço final ficou:",total)

    elif estado == 4:
        taxa = (preco * 8)/100
        total = taxa + preco
        print("O preço final ficou:",total)    
