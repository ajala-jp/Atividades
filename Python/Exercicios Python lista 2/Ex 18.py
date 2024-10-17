sexo = input("Qual o seu sexo: Feminino ou Masculino: ")
altura = float(input("Digite sua altura: "))

if sexo == "Feminino" or sexo == "feminino":
    peso =(62.1*altura)- 44.7
    print("Seu peso ideal com a sua altura é: ",peso)

if sexo == "Masculino" or sexo == "masculino":
    peso = (72.7*altura) - 58
    print("Seu peso ideal com a sua altura é: ",peso)

