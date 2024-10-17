class Círculo:
    def __init__(self, raio):
        self.raio = raio

    def valorRaio(self):
        print(f"Valor do raio: {self.raio}")
    
    def calcularArea(self):
        pi = 3.1415
        area = pi*(self.raio**2)
        print(f"Area do circulo: {area}")

    def calcularCircunferencia(self):
        pi = 3.1415
        circunferencia = 2*pi*(self.raio)
        print(f"O valor da circunferencia é: {circunferencia}")


circulo = Círculo(20)


circulo.calcularArea()
circulo.calcularCircunferencia()
