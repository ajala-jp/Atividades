idade = int(input("Digite sua idade: "))

tempo = int(input("A quantos anos você trabalha: "))

if idade >= 65 or tempo >= 30 or idade >= 60 and tempo >= 25:
    print("Pode se aposentar!")
else:
    print("Você ainda não pode se aposentar")