import random
def sorteioAluno(quantidade):
    listaaluno = []
    for i in range(quantidade):
        aluno = input("Qual o seu nome: ")
        listaaluno.append(aluno)

    alunoaleatorio = random.choice(listaaluno)
    return alunoaleatorio


x = sorteioAluno(3)

print(x)