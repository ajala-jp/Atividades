horastrabalhadas = float(input("Digite quantas horas foram trabalhadas neste mes: "))
horasextras = float(input("Quantas horas extras foram feitas: "))

salariotrabalhado = horastrabalhadas * 32.50

salarioextra = horasextras * 44.50

salariobruto = salarioextra + salariotrabalhado

print("Seu salário bruto total deste mês é: ",salariobruto)

salarioliquido = (salariobruto)-((salariobruto*11)/100)

print("Seu salário líquido ao final do mês é: ",salarioliquido)