alunos = [("Joãoo", 5.0),("Maria",9),("Pedro Felipe Mendes Martins",5),("Ana",12.0)]
cont = 0
cont1 = -1
maior = 0
for i in range(len(alunos)):
    if alunos[cont][1] > alunos[cont1][1]:
        
        maior = alunos[cont]
        cont1 -= 1
    elif alunos[cont1][1] > alunos[cont][1]:
        cont += 1
        maior = alunos[cont1]
    
print("O aluno com a maior nota é o fodão: ",maior)