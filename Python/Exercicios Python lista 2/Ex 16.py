horatrabalhada = float(input("Quantas horas foram trabalhadas: "))

hora = 40.50

horaganha = horatrabalhada * hora
print(horaganha)

if horaganha > 2500:
    horacomdesconto = (horaganha * 11)/100
    horatotalganha = horaganha - horacomdesconto

    print("O seu salário liquido com desconto ficou: ",horatotalganha)

else:
    print("O seu salário liquido foi: ", horaganha)