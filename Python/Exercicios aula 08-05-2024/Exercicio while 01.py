num = int(input("Digite um número: "))

it = 1

while it < 11:
    print(num * it)
    it = it +1

    
print("--"*10)


for multiplicador in range(1,11):
    resultado = multiplicador * num
    print(resultado)