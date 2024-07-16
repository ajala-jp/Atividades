try:
    num = int(input('Informe um número: '))
    i = 2
    if num >= 1:
        while i < num:
            if num % i == 0:
                print(f'O número {num} não é primo')
                break
                
                
            else:
                print(f'O número {num} é primo')
                break
           
    else:
        exit()        


except:
    print('Número inválido')