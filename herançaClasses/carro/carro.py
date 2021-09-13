class Carro():
     def __init__(self, consumo = None, tanque = 0):
          self.consumo = consumo
          self.tanque = tanque

     def mover(self):
          distancia = float(input("Informe quantos quilômetros percorreu: "))

          tanqueFinal = 0

          while distancia > 1:
               if self.tanque < 0:
                    break
               else:
                    tanqueFinal = self.tanque - distancia
          
          return tanqueFinal

     def gasolina(self, tanqueFinal):
          tanqueAtual = tanqueFinal

          return tanqueAtual

     def abastecer(self):
          qtdLitros = int(input("Quantos litros deseja abastecer ? "))

#Não consigo fazer agora na aula, terminar depois em casa


