contrato = int(4000)
ano_aumentado = int(2020)
porcentagem_aumento = 1.5
salarioatualizado = contrato + (contrato * porcentagem_aumento/100)
print(f"O salário em {ano_aumentado} foi",salarioatualizado)

ano_desejado = int(input("Informe o ano em que deseja saber o salário: "))

while ano_aumentado < ano_desejado:
    porcentagem_aumento *= 2
    salarioatualizado = salarioatualizado + (salarioatualizado * porcentagem_aumento/100)
    ano_aumentado += 1
    print(f"O seu salário em {ano_aumentado} foi {salarioatualizado:.2f}")
    
    
    if ano_aumentado == ano_desejado:
        break

