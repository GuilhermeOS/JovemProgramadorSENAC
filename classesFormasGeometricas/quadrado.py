class Quatrolados():
    def __init__(self, L1, L2):
        self.L1 =  L1
        self.L2 =  L2

    def areaQuadrado(self):
        return self.L1 * self.L2

    def calcularPerimetro(self):
        return self.L1 + self.L1 + self.L2 + self.L2

    def quadradoOuRetangulo(self):
        tipo = " "
        if self.L1 == self.L2:
            tipo = "Quadrado"
        else:
            tipo = "Retângulo"
        
        return tipo

