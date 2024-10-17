n = [10,20,30,50,70,80,90,110,200,950]
m=[]
i=0

while i < len(n):
    m.append(n[i]*5)
    i += 1
print(m)

print("-----"*10)

lista1 = []
lista2 = []
quantitade = int(input("Digite uma quantidade: "))

for item in range(quantitade):
    num=int(input("Digite um número: "))
    lista1.append(num)
    lista2.append(num*5)

print(lista1)
print(lista2)

print("-----"*10)

lista3=[10,20,30,50,70,80,90,110,200,950]
lista4=[]
q = 0

for item in lista3:
    lista4.append(lista3[q]*5)
    q +=1
    
print(lista4)

tupla = () #USA PARENTESES, UMA TUPLA NUNCA PODE SER MUDADA OU MELHOR, NUNCA MUDA
listas = [] #USA COLCHETES, PODE ADICIONAR OU REMOVER
dicionario = {} #USA CHAVES