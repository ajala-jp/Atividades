import random
listanumber = []
def sorteio():
    
    for i in range(5):
        numero = random.randint(1,100)
        listanumber.append(numero)
    return listanumber

def somaPar():
    soma = 0
    for i in listanumber:
        if i % 2 == 0:
            soma += i
    return soma

sorteio()    
x = somaPar()

print(x)