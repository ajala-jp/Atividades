# Entrada do usuário
area_pintada = float(input("Digite a área a ser pintada (em metros quadrados): "))

# Cálculos
quantidade_tinta = area_pintada / 6

# Preços
preco_latas = ((quantidade_tinta // 18) + 1) * 80.00
preco_galoes = ((quantidade_tinta // 3.6) + 1) * 25.00

# Resultados
print(f"Quantidade de tinta necessária: {quantidade_tinta:} litros")
print(f"Opção 1: Latas de 18 litros - Preço: R$ {preco_latas}")
print(f"Opção 2: Galões de 3,6 litros - Preço: R$ {preco_galoes}")
