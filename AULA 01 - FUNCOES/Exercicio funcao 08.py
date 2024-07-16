def pesopeixe(quantidade, peso):
    
    
    if peso > 50:
        multa = 0
        excedido = peso - 50
        for item in range(excedido):
            multa += 4.00
        print(f"Peso excedido: {excedido} KG, a multa foi de R$ {multa}")
    else:
        print(f"A quantidade de peixe foi {quantidade} e o peso total dos peixes foi {peso}, está nos padrões da lei!")

pesopeixe(50,50)