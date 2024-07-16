def piramide(n):
    
    carac = "*"
    for i in range(n):
        
        print(" "*(6-i),carac)      
        carac += "*"*2

piramide(6)