def media(num1,num2,num3,letra):
    
    if letra == "A" or letra == "a":
        media = (num1+num2+num3)/3
        return media
    
    elif letra == "P" or letra =="p":
        media = (num1+num2+num3)/(5+3+2)
        return media
    
print(media(20,30,40,"P"))