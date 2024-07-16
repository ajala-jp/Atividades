salario_base = float(input("Digite o salario base: "))

gratificacao = (salario_base * 5)/100

desconto = (salario_base * 7)/100

total = (salario_base + gratificacao) - desconto

print("O salario ao final sera de: ",total)