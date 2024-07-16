valor_produto = float(input("Digite o valor do produto: "))
 
desconto = (valor_produto * 10)/100
 
valor_produto_descontado = valor_produto - desconto
 
print("O valor do produto com desconto de 10% é de: ", valor_produto_descontado)
 
parcela = valor_produto/3
 
print("O valor parcelado em 3x sem juros será de: ",parcela)
 
comissao = (valor_produto_descontado*5)/100


print("O funcionario receberá 5% pelo valor da venda a vista com o desconto, a comissão será de:",comissao)

comissao_sem_desconto = (valor_produto*5)/100

print("O funcionario receberá 5% pelo valor da venda parcelado, a comissão será de:",comissao_sem_desconto)