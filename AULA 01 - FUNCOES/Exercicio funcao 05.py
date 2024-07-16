def somaImposto(taxaImposto,custo):
    taxa = (taxaImposto / 100)*custo
    liquido = custo + taxa
    return  liquido

resultado = somaImposto(5,2000)

print(resultado)