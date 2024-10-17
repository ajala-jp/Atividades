def financiamento():
    valor_veiculo = float(input("Qual o valor do veículo: "))
    entrada = float(input("Informe um valor de entrada: "))
    taxa_juros = float(input("Informe o valor da taxa: "))
    financiar = int(input("Informe em quantas vezes gostaria de financiar: "))
    valor_total = entrada *(1+ taxa_juros/100) ** financiar
    valortotal_pago = valor_total + valor_veiculo
    parcela = valortotal_pago / financiar
    print(f"O valor total pago foi {valortotal_pago:.2f}, o valor total dos juros foi {valor_total:.2f} e o valor das parcelas mensalmente é de {parcela:.2f}")

financiamento()