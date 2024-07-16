nome = str(input("Digite seu nome: "))
dia_vencimento = int(input("Digite o dia do vencimento por favor"))
while dia_vencimento > 30:
   dia_vencimento = int(input("Digite o dia do vencimento novamente por favor"))
mes_vencimento = str(input("Por gentileza, digite o mes do vencimento"))

valor_fatura = str(input("Por favor, digite o valor da sua fatura: "))

print("Olá,",nome)
print("A sua fatura com o vencimento em",dia_vencimento,"de",mes_vencimento,"no valor de R$",valor_fatura,"está fechada.")
    
    
    
    

