def calcularTempo(minutos):
    if minutos <= 15:
        return 0
    else:
        valor_hora = 9.00
        horas = minutos / 60
        temporestante = minutos - 60
        valor_hora += (temporestante // 60)* 1.50
        if temporestante % 60 > 0:
            valor_hora += 1.50
        pis = (0.033 * valor_hora)
        cofins = (0.020 * valor_hora)
        icms = (0.17 * valor_hora)
        total = valor_hora
        print(f"Tempo {horas:.2f} horas")
        print(f"PIS R${pis:.2f}")
        print(f"CONFINS R${cofins:.2f}")
        print(f"ICMS R${icms:.2f}")
        print(f"IMPOSTOS R${pis+cofins+icms:.2f}")
        print(f"Total R$ {total:.2f}")
        
        
        
    
    
print(calcularTempo(240))