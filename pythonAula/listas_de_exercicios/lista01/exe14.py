'''
    Tendo como dados de entrada a altura e o sexo de uma pessoa ("M" masculino e "F"
    feminino), construa um algoritmo que calcule seu peso ideal, utilizando as
    seguintes fórmulas:
        a. para homens: (72.7 * h) - 58
        b. para mulheres: (62.1 * h) - 44.7
'''

sexo = str(input("Informe o sexo da pessoa (M/F): "))
altura = float(input("Informe a  altura: "))
if sexo == "M" or sexo == "m":
    pesoIdeal = (72.7 * altura) - 58
else:
    pesoIdeal = (62.1 * altura) - 44.7

print(f"O pesso ideal é {pesoIdeal:.2f}!")