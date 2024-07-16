
try:
    def numeros(a:int):
        numeros = str(a)  
        print(len(numeros))
        return numeros

    componentes = int(numeros(input("Informe um número: ")))

except ValueError:
    print("Valor inválido")


