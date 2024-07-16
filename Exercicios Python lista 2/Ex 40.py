ganho_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe quantas horas foram trabalhadas: "))

#Salário bruto
salario_bruto = ganho_hora * horas_trabalhadas
print("O salário bruto é:",salario_bruto)

#Valor pago ao INSS
inss = (salario_bruto * 8)/ 100
print("O valor pago ao INSS foi:",inss)

#Valor pago ao imposto de renda
imposto = (salario_bruto * 11)/ 100
print("O valor pago ao imposto de renda foi:",imposto)

#Valor pago ao sindicato
sindicato = (salario_bruto * 5)/100
print("O valor pago ao sindicato foi:",sindicato)

#Valor líquido
liquido = salario_bruto - inss - imposto - sindicato
print("O salário líquido é:",liquido)
