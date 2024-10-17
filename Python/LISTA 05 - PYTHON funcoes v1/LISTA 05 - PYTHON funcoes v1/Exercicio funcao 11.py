def operacao(num1, num2, simbolo):
    
    if simbolo == "+":
        operacao = num1 + num2
        return operacao
    
    elif simbolo == "-":
        operacao = num1 - num2
        return operacao
    
    elif simbolo == "/":
        operacao = num1 / num2
        return operacao

    elif simbolo == "*":
        operacao = num1 * num2
        return operacao

    
    
print(operacao(10,10,"*"))
