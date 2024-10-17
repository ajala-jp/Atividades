print("--"*20)
print("Especificação || Código || Preço   ")
print("   Hot dog        100      12.00")
print("  X-Salada        102      18.50")
print("  X-BACON         103      25.50")
print("  X-Burguer       104      17.00")
print("Suco de laranja   105      9.50 ")
print(" Refrigerante     106      6.00")
print("--"*20)

codigo = int(input("Digite o código do pedido: "))
quantidade = int(input("Informe quantos gostaria de comprar: "))

if codigo == 100:
    valor = quantidade * 12.00
    print("O valor a ser pago é:",valor)

elif codigo == 102:
    valor = quantidade * 18.50
    print("O valor a ser pago é:",valor)

elif codigo == 103:
    valor = quantidade * 25.50
    print("O valor a ser pago é:",valor)

elif codigo == 104:
    valor = quantidade * 17.00
    print("O valor a ser pago é:",valor)

elif codigo == 105:
    valor = quantidade * 9.50
    print("O valor a ser pago é:",valor)
elif codigo == 106:
    valor = quantidade * 6.00
    print("O valor a ser pago é:",valor)