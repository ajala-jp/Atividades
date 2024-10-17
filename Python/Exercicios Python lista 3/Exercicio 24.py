soma = 0

for i in range(1,1001):
    if i % 3 == 0:
        soma += i
    elif i % 5 == 0:
        soma += i

print(soma)