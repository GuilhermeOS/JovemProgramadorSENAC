
class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def areaCirculo(self):
        area = 3.14 * (self.raio**2)
        
        return area

    def perimetroCirculo(self):
        perimetro = (2 * 3.14) * self.raio

        return perimetro
