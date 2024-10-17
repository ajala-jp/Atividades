valor_hora = float(input("Quanto ganha por hora: "))

horas_trabalhados = float(input("Digite quantas horas foi trabalhada nesse mês: "))

valor_bruto = valor_hora * horas_trabalhados

aumentado = (valor_bruto * 10) /100

total = aumentado + valor_bruto

print("O total recebido pelas horas trabalhadas foi: ", total)

