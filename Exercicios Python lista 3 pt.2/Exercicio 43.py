cont = 0
import random

numeroaleatorio = int(random.uniform(1,100))

while True:
    numerodousuario = int(input("Informe um valor de 1 a 100: "))
    cont +=1
    if numerodousuario < numeroaleatorio:
        print(f"O número {numerodousuario} é menor que o número aleatório!")
    elif numerodousuario > numeroaleatorio:
        print(f"O número {numerodousuario} é maior que o número aleatório!")
    
    else:
        print("--"*40)
        print(f"ACERTOU, ACERTOU, ACERTOU!!! O NÚMERO {numerodousuario} É O NÚMERO MISTERIOSOOOOOO!!! COM APENAS {cont} TENTATIVAS!!")
        print("--"*40)
        break