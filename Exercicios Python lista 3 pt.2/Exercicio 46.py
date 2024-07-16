chico = 1.70
malditodoze = 1.20
cont = 0

while True:
    chico += 0.02
    malditodoze += 0.03
    cont+=1
    if malditodoze > chico:
        break

print(f"{chico:.2f}")
print(f"{malditodoze:.2f}")
print(f"A quantidade de anos em que o Zé será mais alto que o Chico é {cont}")



