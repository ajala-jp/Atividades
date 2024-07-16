somaquadrado = 0
somanaturais = 0
for i in range(1,10+1):
    quadrado = i **2
    somaquadrado += quadrado
    somanaturais+= i

naturaisquadrado = somanaturais **2

resultado = naturaisquadrado - somaquadrado

print(resultado)


