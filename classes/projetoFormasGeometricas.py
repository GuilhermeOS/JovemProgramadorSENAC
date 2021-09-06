from circulo import *
from triangulo import *
from quadrado import *


print("--- FORMAS DISPONÍVEIS ---")
print("1 - Quadrado\n2 - Círculo\n3 - Triângulo")

formaEsolhida = int(input("Digite o número referente a forma desejada: "))

print("--- CÁLCULOS DISPONÍVEIS ---")
print("1 - Area\n2 - Perimetro")

calculo = int(input("Digite o número referente ao calculo escolhido: "))

if formaEsolhida == 1:
    if calculo == 1:
        lado1 = int(input("Informe o tamanho do primeiro lado: "))
        lado2 = int(input("Informe o tamanho do segundo lado: "))

        lados = Quatrolados(lado1, lado2)

        areaQuadrado = lados.areaQuadrado()

        print(f"A área do quadrado é: {areaQuadrado}")
    elif calculo == 2:
        lado1 = int(input("Informe o tamanho do primeiro lado: "))
        lado2 = int(input("Informe o tamanho do segundo lado: "))

        lados = Quatrolados(lado1, lado2)  

        perimetroQuadrado = lados.calcularPerimetro()

        print(f"O perímetro do quadrado é de: {perimetroQuadrado}")
elif formaEsolhida == 2:
    if calculo == 1:
        raioCirculo = int(input("Informe o raio do círculo: "))

        raio = Circulo(raioCirculo)

        areaCirculo = raio.areaCirculo()

        print(f"A área do círculo é {areaCirculo}")
    elif calculo == 2:
        raioCirculo = int(input("Informe o raio do círculo: "))

        raio = Circulo(raioCirculo)

        perimetroCirculo = raio.perimetroCirculo()

        print(f"A área do círculo é {perimetroCirculo}") 
elif formaEsolhida == 3:
    if calculo == 1:
        base = int(input("Informe a base do triângulo: "))
        altura = int(input("Informe a altura do triângulo: "))

        triangulo = Triangulo(base = base, altura = altura, lado1=None, lado2=None, lado3=None)

        areaTriangulo = triangulo.areaTriangulo()

        print(f"A área do triângulo é {areaTriangulo}")
    elif calculo == 2:
        lado1 = int(input("Informe o primeiro lado do triângulo: "))
        lado2 = int(input("Informe o segundo lado do triângulo: "))
        lado3 = int(input("Informe o terceiro lado do triângulo: "))

        triangulo = Triangulo(base = None, altura = None,  lado1 = lado1, lado2 = lado2, lado3 = lado3)

        perimetroTriangulo = triangulo.perimetroTriangulo()

        print(f"O perímetro do triângulo é {perimetroTriangulo}") 
else:
    print("Opção inválida!")  

print(Quatrolados.__doc__)