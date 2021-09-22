'''
    Faça um algoritmo que leia um n° inteiro e mostre uma mensagem indicando se este
    número é par ou impar, e se é positivo ou negativo.
'''

numero = int(input("Digite um número qualquer: "))

if numero > 0 and numero % 2 == 0:
    print(f"{numero} é positivo e par!")
elif numero > 0 and numero % 2 != 0:
    print(f"{numero} é positivo e ímpar!")
elif numero < 0 and numero % 2 == 0:
    print(f"{numero} é negativo e par!")
elif numero < 0 and numero % 2 != 0:
    print(f"{numero} é negativo e ímpar!")