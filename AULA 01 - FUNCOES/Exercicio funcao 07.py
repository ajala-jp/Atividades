def salariodepobre(salarioporhora,horastrabalhadas):
    total = 0

    if horastrabalhadas > 40:
        horastotal = horastrabalhadas - 40
        porcentagem = horastotal * 50
        taxa = (porcentagem / 100)*salarioporhora
        salariototal = salarioporhora * 40
        total = taxa + salarioporhora + salariototal
        print(total)

    elif horastrabalhadas <= 40:
        total= salarioporhora * horastrabalhadas
        print(total)
    
    return total

salariodepobre(20,39)