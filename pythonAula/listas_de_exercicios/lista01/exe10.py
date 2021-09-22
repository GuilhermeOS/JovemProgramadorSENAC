'''
    A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: 
    lata de 350ml, garrafa de 600ml e garrafa  de 2 litros. Se um comerciante
    compra uma determinada quantidade de cada formato, faça um algoritmo para
    calcular quantos litros de refrigerante ele comprou.
'''

lataPequena = 350 / 1000
lataMedia = 600 / 1000
garrafa = 2

quantidadePequenas = int(input("Informe quantas garrafas de 350ml foram compradas: "))
quantidadeMedias = int(input("Informe quantas garrafas de 650ml foram compradas: "))
quantidadeGarrafas = int(input("Informe quantas garrafas de 2L foram compradas: "))

litrosTotal = (lataPequena * quantidadePequenas) + (lataMedia * quantidadeMedias) + (garrafa * quantidadeGarrafas)

print(f"Foram comprados {litrosTotal} litros de bebida ao total!")