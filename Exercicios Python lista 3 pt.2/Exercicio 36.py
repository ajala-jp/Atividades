try:
    nota_aluno = []
    cont = 1
    qtd = 0



    for i in range(1,2+1):
        print('Aluno',cont)
        nota1 = float(input('Informe sua primeira nota: '))
        nota2 = float(input('Informe sua segunda nota: '))
        nota3 = float(input('Informe sua terceira nota: '))
        nota4 = float(input('Informe sua quarta nota: '))
        if nota1 and nota2 and nota3 and nota4 >=0 and nota1 and nota2 and nota3 and nota4 < 10:
        
            cont+=1
            media = (nota1 + nota2 + nota3 + nota4) /4
            nota_aluno.append(media)

        else:
            
            exit()

    for i in nota_aluno:
        if i >= 7:
            qtd +=1
        else:
            continue

    print(f'O númeor de alunos com a nota maior ou igual a 7, é: {qtd}')

except:
    print('Valor inválido')
    exit()