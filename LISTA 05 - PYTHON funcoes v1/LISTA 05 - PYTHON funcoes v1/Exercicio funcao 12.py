def numeros(num1: int, num2: int):
    soma = 0
    for i in range(num1,num2+1):
        soma +=  i
    print(soma)
        
    return soma


numeros(1,10)