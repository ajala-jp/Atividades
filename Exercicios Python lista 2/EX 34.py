preco = float(input("Informe o preço do produto: "))

if preco < 50:
    aumento = (preco * 5) / 100
    total = aumento + preco
    print("O novo valor do produto é:",total)
elif preco >= 50 and preco <= 100:
    aumento = (preco * 10) / 100
    total = aumento + preco
    print("O novo valor do produto é:",total)

elif preco > 100:
    aumento = (preco * 15) / 100
    total = aumento + preco
    print("O novo valor do produto é:",total)