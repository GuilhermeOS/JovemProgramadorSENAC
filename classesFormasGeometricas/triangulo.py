class Triangulo():
    def __init__(self, lado1, lado2, lado3, base = None, altura = None):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def areaTriangulo(self):
        area = (self.base * self.altura) / 2

        return area

    def perimetroTriangulo(self):
        perimetro = self.lado1 + self.lado2 + self.lado3

        return perimetro