numeros = [10,40,85,41,60,95,75,42,51,63,95,4,52,44,41,62,85]

soma = sum(numeros[0:5]) + sum(numeros[8:20])

numeros.sort(reverse=bool) #Ordena de forma decrescente sem usar o print (reverse=bool)
print(sorted(numeros,reverse=True)) # Ordenar de forma decrescente usando o print
print(sorted(numeros)) #Sorted ordena de forma crescente usando o print

print(soma)

num2 = 6.85452
num = 5.5625422
num = "{:.2f}".format(num) #formata o número, mudando somente o modo de exibição e nao modificando o numero

print(round(num2,2)) #limita o numero de casas após a virgula, mas modifica o numero. Round arredonda o numero
print(num)
