salario = float(input("Digite qual o seu salário: "))

vinteporcento = (salario * 20) /100

emprestimo = float(input("Qual o valor do empréstimo: "))

if emprestimo > vinteporcento:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")