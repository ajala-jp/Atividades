class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        print(f"Perímetro: {perimetro}")

    def getMaiorLado(self):
        if self.ladoC > self.ladoB and self.ladoC > self.ladoA:
            print(f"Lado C é o maior: {self.ladoC}")
        
        elif self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print(f"Lado A é o maior: {self.ladoA}")

        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print(f"Lado B é o maior: {self.ladoB}")
        
        else:
            print("Os lados são iguais")

triangulo = Triangulo(1,1,1)

triangulo.calcularPerimetro()

triangulo.getMaiorLado()