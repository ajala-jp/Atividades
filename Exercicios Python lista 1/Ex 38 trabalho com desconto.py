dias = int(input("Quantos dias foi trabalhado este mes: "))

bruto= dias * 30

descontado = int(8)

liquido1 = (bruto * descontado)/100

liquido2 = bruto - liquido1

print("O salario liquido no final do mes sera de: ",liquido2)

