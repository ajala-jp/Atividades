#Função com argumento

def hello():
    cont = 0
    while True:
        print("Hello")
        cont += 1
        if cont == 10:
            break



def soma(a,b):
    soma = a + b
    return soma

x = int(input("Informe um número: "))


y = int(input("Informe outro número: "))

res = soma(x,y)

print(res)




def ola(nome):
   
    if nome == "Pedro Felipe Mendes Martins" or nome == "pedro felipe mendes martins":
        print(f"Olá {nome}, seu vacilão")
    else:
        print(f"Olá {nome}")
        







