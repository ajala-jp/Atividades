votojoao = 0
votocarlinhos = 0
votopereira = 0
votoednaldo = 0
votonulo = 0
votobranco = 0
votostotal = 0
while True:
    print("0 - Sair")
    print("1 - João")
    print("2 - Carlinhos")
    print("3 - Pereira")
    print("4 - Ednaldo")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    


    num = int(input("Informe o número do candidato em que deseje votar!\n"))
    if num == 1:
        print("Você votou no João!")
        votojoao += 1 
        votostotal += 1

    elif num == 2:
        print("Você votou no Carlinhos!")
        votocarlinhos += 1
        votostotal += 1

    elif num == 3:
        print("Você votou no Pereira!")
        votopereira +=1
        votostotal += 1

    elif num == 4:
        print("Você votou no Ednaldo!")
        votoednaldo += 1
        votostotal += 1
    
    elif num == 5:
        print("Você votou nulo!")
        votonulo +=1
        votostotal += 1
    
    elif num == 6:
        print("Você votou em branco!")
        votobranco += 1
        votostotal += 1
    
    elif num == 0:
        break

if votostotal > votonulo:
    diferencanulo = votostotal - votonulo
    diferencanulo = (diferencanulo/votonulo)*100
else:
    diferencanulo = votonulo-votostotal
    diferencanulo = (diferencanulo/votonulo)*100

if votostotal > votobranco:
    diferencabranco = votostotal - votobranco
    diferencabranco = (diferencabranco/votostotal)*100 

else:
    diferencabranco = votobranco - votostotal
    diferencabranco = (diferencabranco/votostotal)*100   

print(f"A quantidade de pessoas que votaram no João foi: {votojoao}")
print(f"A quantidade de pessoas que votaram no Carlinhos foi: {votocarlinhos}")
print(f"A quantidade de pessoas que votaram no Pereira foi: {votopereira}")
print(f"A quantidade de pessoas que votaram no Ednaldo foi: {votoednaldo}")
print(f"A percentagem de votos nulos sobre os votos totais foi: {diferencanulo:.2f}% ")
print(f"A percentagem de votos em branco sobre os votos totais foi: {diferencanulo:.2f}% ")

