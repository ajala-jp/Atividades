import math

x1 = int(input("X1: "))
x2 = int(input("X2: "))
y1 = int(input("Y1: "))
y2 = int(input("Y2: "))


distancia = math.sqrt((x1 - x2)**2)+((y1-y2)**2)

if distancia >= 10:
    print("longe")
else:
    print("Perto")




