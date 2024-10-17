#NUMEROS
numeros = [6,8,7,5.5]


#FRUTAS
frutas = ["Mamao", "Melancia", "Goiaba", "Abacaxi", "Uva", "Melao"]

print(frutas[-3])

print("As melhores frutas são:",frutas[0:2])

print(sum(numeros)) #sum é a soma dos numeros

print(max(numeros)) #max pega o maior número

print(min(numeros)) #min pega o menor número

print("A média dos numeros é:",sum(numeros)/len(numeros))

numeros.append(45)
numeros.append(99) #append adiciona algo no final da lista
print(numeros)
numeros.pop(-3) #pop remove o último item colocado na lista, ou coloque a posição do número que deseja retirar dentro das ()

numeros.insert(0,56) #insert adiciona um número na posição desejada, primeiro coloque a posição e depois coloque o número desejado, por exemplo (0,56) posição 0 e o número 56

print(numeros)

numeros.remove(7) #remove remove um número específico

numeros.sort()
print(numeros)

print(numeros.index(45)) #index, mostra a posição do número ou valor da variavel


print(sum(numeros[0:3]))
