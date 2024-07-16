n = int(input("Digite o valor de n: "))

for p in range(1,n*2):
    if p % 2 == 1:
      print(p)
    
m = int(input("Digite o valor de m: "))
i = 1
j = 0

while j < m:
   print(i)
   i += 2
   j += 1