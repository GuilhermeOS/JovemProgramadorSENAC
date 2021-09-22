'''
    Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit.
    Faça um algoritmo para ler a temperatura Celsius e imprimi-la em Fahrenheit 
    (pesquise como fazer este tipo de conversão).
'''

celsius = float(input("Informe a temperatura em Celsius: "))

conversao = (celsius * 1.8) + 32

print(f"{celsius}° em Fahrenheit é °{conversao:.2f}!")