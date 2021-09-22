'''
    Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos
    dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365
    dias. Ex: uma pessoa com 19 anos possui 6935 dias devida.
'''

nome = str(input("Informe seu nome a seguir: "))
idade = int(input("Informe a sua idade: "))

diasVida = idade * 365

print(f"{nome} você tem {diasVida} dias de vida!")

#Parece que ela só tem mais essa quantidade de dias pela forma como eu escrevi :'(