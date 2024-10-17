pao = 0.12

broa = 1.50

pao_vendidos = int(input("Quantos pães foram vendidos: "))

total_pao = pao_vendidos*pao

broa_vendidas = int(input("Quantas broas foram vendidas: "))

total_broa = broa_vendidas*broa

total_ganho = total_broa+total_pao

print("O valor total vendido foi: ",total_ganho)

poupanca = (total_ganho*10)/100

print("O valor que entrará na poupança será: ",poupanca)

