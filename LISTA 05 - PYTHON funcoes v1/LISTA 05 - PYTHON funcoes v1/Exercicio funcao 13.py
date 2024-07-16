def exponenciacao(x,z):
    expo = x
    for i in range(z-1):
        expo *= x
    print(expo)

exponenciacao(10,2)