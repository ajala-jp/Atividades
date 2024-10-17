numeros = [14,45,20,15,85,23]

numeros.append(5.8)
numeros.append(9.32)
numeros.append(8.47)
numeros.append(2.85)
numeros.append(45.21)
numeros.append(96.52)

numeros.pop()
numeros.pop()

numeros.insert(1,10)
numeros.insert(2,11)

numeros.sort()

print(max(numeros))
print(min(numeros))
print(sum(numeros))
print(sum(numeros)/len(numeros))

numeros.remove(10)

print(numeros.index(11))

print(numeros[4]*numeros[5])


print(sorted(numeros,reverse=True)) #ou usar numeros.sort(reverse=bool) e depois o print